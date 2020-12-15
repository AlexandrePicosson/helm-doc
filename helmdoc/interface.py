import click
import yaml
import os


def write_head(file):
    pass


def appendValue(values, base_value=""):
    string = ""
    if isinstance(values, dict):
        itr = values.items()
        islist = False
    elif isinstance(values, list):
        itr = enumerate(values)
        islist = True

    for item, value in itr:
        if isinstance(values[item], dict) and values[item] is not {}:
            if islist:
                string += appendValue(values[item], base_value=f"{base_value}[{item}].")
            else:
                string += appendValue(values[item], base_value=f"{base_value}{item}.")
        elif isinstance(values[item], list) and len(values[item]) > 0:
            string += appendValue(values[item], base_value=f"{base_value}{item}")
        else:
            if values[item] == "":
                values[item] = '""'
            string += f" {base_value}{item} | ... | `{values[item]}` \n"
    return string


@click.command()
@click.argument("chart", type=click.Path(exists=True))
@click.option("-o", "--output", default="README.md", show_default=True)
def cli(chart, output):
    values_path = os.path.join(chart, "values.yaml")
    if not os.path.isfile(values_path):
        raise click.BadParameter(
            "There is no values.yaml in this folder", param=chart, param_hint="INPUT"
        )

    with open(values_path, "r") as values_file:
        values = yaml.load(values_file, Loader=yaml.FullLoader)

    val = """
Parameter | Description | Default
--- | --- | ---
"""
    val += appendValue(values)

    click.echo(val)
