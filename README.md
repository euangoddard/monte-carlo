# Monte Carlo Simulation

A simple Monte Carlo simulation to forecast the time required to complete a number of tasks given a historic set of durations.

## Running

Launch the CLI service with:

```bash
docker compose run cli python simulation.py 1 2 3 4
```

Where `1 2 3 4` are the historic durations of the tasks.

This will give you an output like this:

```
Simulating 10 tasks with 10000 iterations...

50th percentile total duration: 25.0 days
75th percentile total duration: 27.0 days
85th percentile total duration: 29.0 days
95th percentile total duration: 31.0 days


Distribution of total durations
| Total duration | Count |
|----------------|-------|
|             14 |     9 |
|             15 |    12 |
|             16 |    36 |
|             17 |    91 |
|             18 |   151 |
|             19 |   291 |
|             20 |   407 |
|             21 |   605 |
|             22 |   796 |
|             23 |   943 |
|             24 |  1109 |
|             25 |  1152 |
|             26 |  1093 |
|             27 |   922 |
|             28 |   807 |
|             29 |   569 |
|             30 |   409 |
|             31 |   260 |
|             32 |   183 |
|             33 |    95 |
|             34 |    39 |
|             35 |    14 |
|             36 |     5 |
|             37 |     2 |
```

## Options

To see a list of available options, run:

```bash
docker compose run cli python simulation.py --help
```

You will see this kind of output:

```
Usage: simulation.py [OPTIONS] [DURATIONS]...

  Run a Monte Carlo simulation to estimate the time required to complete a set
  of tasks based off past task durations.

Options:
  -t, --tasks INTEGER          Number of tasks to simulate
  -i, --iterations INTEGER     Number of iterations in the simulation
  --period [hours|days|weeks]  Period to consider for the durations
  -p, --percentile INTEGER     Percentiles to calculate
  -o, --output [md|csv|tsv]    Output format for the breakdown
  --help
```

### Tasks

Description: Specifies the number of tasks to simulate.
Default: `10`
Usage: `--tasks 20z or `-t 20`

### Iterations

Description: Defines the number of iterations to run in the simulation.
Default: `10000`
Usage: `--iterations 5000` or `-i 5000`

### Period

Description: Sets the period to consider for the durations. The available choices are hours, days, and weeks.
Default: `days`
Usage: `--period weeks`

### Percentiles

Description: Specifies the percentiles to calculate. This option can be provided multiple times to include multiple percentiles.
Default: `[50, 75, 85, 95]`
Usage: `--percentile 50 --percentile 90` or `-p 50 -p 90`

### Time distribtion output

Description: Determines the output format for the breakdown. The available choices are `md` (Markdown), `csv` (Comma-Separated Values), and `tsv` (Tab-Separated Values).
Default: `md`
Usage: `--output csv` or `-o csv`

### Past task Ddrations

Description: A list of integers representing the durations of past tasks. This is a positional argument and can accept multiple values.
Usage: `10 20 30 40`

## Example Usage

To run the simulation with 20 tasks, 5000 iterations, considering durations in weeks, calculating the 90th percentile, and outputting the results in CSV format, you would use the following command:

```bash
python simulation.py --tasks 20 --iterations 5000 --period weeks --percentile 90 --output csv 10 20 30 40
```

This command will simulate 20 tasks over 5000 iterations, considering the durations in weeks, calculate the 90th percentile, and output the results in CSV format based on the provided durations of 10, 20, 30, and 40.
