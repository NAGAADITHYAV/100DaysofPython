"""Compare average annual interest as a percentage of original principal."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, PercentFormatter


def plot_interest(principal=10000, years=40, output=None):
    """Plot total interest / principal / years, expressed as a percentage."""
    if principal <= 0 or years < 1:
        raise ValueError("Principal must be positive and years must be at least 1.")

    # Start at year 1 because dividing by zero years is undefined.
    year_numbers = list(range(1, years + 1))
    simple_interest = [18.0 for year in year_numbers]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(year_numbers, simple_interest, linestyle="--", linewidth=2,
            color="black", label="Simple interest: 18% per year")
    for rate in (0.10, 0.08, 0.07, 0.065, 0.06):
        compound_interest = [100 * ((1 + rate) ** year - 1) / year
                             for year in year_numbers]
        ax.plot(year_numbers, compound_interest,
                label=f"Compound interest: {rate * 100:g}% (compounded annually)")
    ax.set(title="Average annual interest relative to original principal",
           xlabel="Years invested", ylabel="Total interest / principal / years (%)")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
    ax.set_xlim(0, max(years, 2))
    ax.set_ylim(bottom=0)
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()

    output = Path(output) if output else Path(__file__).with_name("interest_comparison.png")
    fig.savefig(output, dpi=150)
    print(f"Graph saved to {output.resolve()}")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--principal", type=float, default=10000)
    parser.add_argument("--years", type=int, default=40)
    parser.add_argument("--output", help="Output path (default: interest_comparison.png beside this script).")
    args = parser.parse_args()
    if args.principal <= 0 or args.years < 1:
        parser.error("Principal must be positive and years must be at least 1.")
    plot_interest(args.principal, args.years, args.output)
