import click
from numpy.random import choice as random_choice
from numpy import percentile


@click.command
@click.option("--tasks", "-t", default=10, help="Number of tasks to simulate")
@click.option(
    "--iterations",
    "-i",
    default=10000,
    help="Number of iterations in the simulation",
)
@click.option(
    "--period",
    type=click.Choice(
        ["hours", "days", "weeks"],
    ),
    default="days",
    help="Period to consider for the durations",
)
@click.option(
    "--percentile",
    "-p",
    "percentiles",
    multiple=True,
    default=[50, 75, 85, 95],
    help="Percentiles to calculate",
)
@click.option(
    "--output",
    "-o",
    "output_format",
    type=click.Choice(
        ["md", "csv", "tsv"],
    ),
    default="md",
    help="Output format for the breakdown",
)
@click.argument("durations", nargs=-1, type=int)
def main(
    durations: list[int],
    tasks: int,
    iterations: int,
    period: str,
    percentiles: list[int],
    output_format: str,
):
    """
    Run a Monte Carlo simulation to estimate the time required to complete a set of
    tasks based off past task durations.
    """
    click.echo(f"Simulating {tasks} tasks with {iterations} iterations...\n")

    total_durations = []
    for _ in range(iterations):
        sampled_tasks = random_choice(durations, size=tasks, replace=True)
        total_duration = sum(sampled_tasks)
        total_durations.append(total_duration)

    for nth_percentile in percentiles:
        percentile_value = percentile(total_durations, nth_percentile)
        percentile_label = click.style(f"{nth_percentile}th", fg="bright_white")
        percentile_value_period = click.style(
            f"{percentile_value} {period}", fg="bright_blue"
        )
        click.echo(
            f"{percentile_label} percentile total duration: {percentile_value_period}"
        )

    click.echo("\n")

    if output_format == "md":
        _output_distribution_as_markdown(total_durations)
    elif output_format == "csv":
        _output_distribution_as_csv(total_durations)
    elif output_format == "tsv":
        _output_distribution_as_tsv(total_durations)
    else:
        click.error(f"Unknown output format: {output_format}")


def _output_distribution_as_markdown(total_durations: list[int]):
    click.echo("Distribution of total durations")
    click.echo("| Total duration | Count |")
    click.echo("|----------------|-------|")
    for duration, count in _get_durations_with_counts(total_durations):
        click.echo(f"| {str(duration).rjust(14)} | {str(count).rjust(5)} |")


def _output_distribution_as_csv(total_durations: list[int]):
    click.echo("Total duration,Count")
    for duration, count in _get_durations_with_counts(total_durations):
        click.echo(f"{duration},{count}")


def _output_distribution_as_tsv(total_durations: list[int]):
    click.echo("Total duration\tCount")
    for duration, count in _get_durations_with_counts(total_durations):
        click.echo(f"{duration}\t{count}")


def _get_durations_with_counts(total_durations: list[int]):
    for duration in sorted(set(total_durations)):
        count = total_durations.count(duration)
        yield duration, count


if __name__ == "__main__":
    main()
