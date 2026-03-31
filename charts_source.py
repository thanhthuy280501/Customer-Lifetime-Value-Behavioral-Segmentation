"""
charts_source.py
─────────────────────────────────────────────────────────────────────────────
Standalone Python (Matplotlib + Seaborn) versions of every chart used in
Thuy_Nguyen_CLV_Presentation.pptx

Run this file to generate all 3 charts as PNG files you can reuse anywhere.

Install:  pip install matplotlib seaborn pandas numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── Shared style ──────────────────────────────────────────────────────────────
NAVY    = "#0D1B4B"
TEAL    = "#0E7C86"
TEAL2   = "#14A5B3"
AMBER   = "#F59E0B"
GREEN   = "#10B981"
RED     = "#EF4444"
GRAY    = "#64748B"
LGRAY   = "#E2E8F0"
OFFWHITE= "#F4F7FA"

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.spines.left": False,
    "axes.grid":        True,
    "axes.grid.axis":   "y",
    "grid.color":       LGRAY,
    "grid.linewidth":   0.7,
    "axes.facecolor":   "white",
    "figure.facecolor": "white",
    "text.color":       NAVY,
    "axes.labelcolor":  GRAY,
    "xtick.color":      GRAY,
    "ytick.color":      GRAY,
})


# ═════════════════════════════════════════════════════════════════════════════
# CHART 1 — % of Total Revenue by Segment  (Slide 2, bar chart)
# ═════════════════════════════════════════════════════════════════════════════
def chart1_revenue_by_segment():
    segments = ["High Value", "Low Value", "Frequent\nLow Spend", "One-time\nBuyer", "Risky"]
    revenues = [77.1, 16.4, 3.7, 2.5, 0.6]
    colors   = [TEAL, TEAL2, "#5DCFDA", "#A8E6EC", "#D1F4F8"]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(segments, revenues, color=colors, width=0.55, zorder=3)

    # Data labels
    for bar, val in zip(bars, revenues):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.8,
            f"{val}%",
            ha="center", va="bottom", fontsize=11, fontweight="bold", color=NAVY
        )

    ax.set_title("% of Total Revenue by Segment", fontsize=14, fontweight="bold",
                 color=NAVY, pad=14, loc="left")
    ax.set_ylabel("% of Revenue", fontsize=10, color=GRAY)
    ax.set_ylim(0, 90)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=9)

    # Teal top accent bar
    fig.add_artist(plt.Line2D([0, 1], [1, 1], transform=fig.transFigure,
                               color=TEAL, linewidth=4))

    plt.tight_layout()
    plt.savefig("chart1_revenue_by_segment.png", dpi=150, bbox_inches="tight")
    print("Saved: chart1_revenue_by_segment.png")
    plt.show()


# ═════════════════════════════════════════════════════════════════════════════
# CHART 2 — Monthly Order Trend by Segment  (Slide 2, line chart)
# ═════════════════════════════════════════════════════════════════════════════
def chart2_monthly_trend():
    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]

    # Illustrative trend values matching the deck
    # Replace with: df.groupby(['Month','Segment'])['InvoiceNo'].count()
    high_value   = [120, 100, 130, 145, 160, 155, 170, 180, 195, 220, 310, 140]
    one_time     = [ 60,  50,  65,  70,  75,  72,  78,  85,  90, 100, 155,  70]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(months, high_value, color=TEAL,  linewidth=2.5, marker="o",
            markersize=5, label="High Value")
    ax.plot(months, one_time,   color=AMBER, linewidth=2.5, marker="o",
            markersize=5, label="One-time Buyer")

    # November annotation
    nov_idx = months.index("Nov")
    ax.annotate("Peak: Nov", xy=(nov_idx, high_value[nov_idx]),
                xytext=(nov_idx - 1.8, high_value[nov_idx] + 18),
                fontsize=9, color=TEAL, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2))

    ax.set_title("Monthly Order Trend by Segment", fontsize=14, fontweight="bold",
                 color=NAVY, pad=14, loc="left")
    ax.set_ylabel("Number of Orders", fontsize=10, color=GRAY)
    ax.set_ylim(0, 360)
    ax.tick_params(axis="x", labelsize=9, rotation=30)
    ax.tick_params(axis="y", labelsize=9)
    ax.legend(fontsize=9, frameon=False, loc="upper left")

    fig.add_artist(plt.Line2D([0, 1], [1, 1], transform=fig.transFigure,
                               color=TEAL, linewidth=4))

    plt.tight_layout()
    plt.savefig("chart2_monthly_trend.png", dpi=150, bbox_inches="tight")
    print("Saved: chart2_monthly_trend.png")
    plt.show()


# ═════════════════════════════════════════════════════════════════════════════
# CHART 3 — Segment Comparison Table  (used as visual in Slide 2 cards)
#            Rendered here as a styled horizontal bar chart for easy reading
# ═════════════════════════════════════════════════════════════════════════════
def chart3_segment_comparison():
    data = {
        "Segment":         ["High Value", "Low Value", "One-time Buyer",
                            "Freq. Low Spend", "Risky"],
        "% Customers":     [19.9, 49.3, 23.5, 5.2, 1.2],
        "% Revenue":       [77.1, 16.4,  2.5,  3.7, 0.6],
        "Avg Revenue (£)": [10879, 934, 297, 1997, 1500],
        "Avg Orders":      [23, 4, 1, 13, 7],
        "Cancel Rate (%)": [17, 13, 0, 20, 63],
    }
    df = pd.DataFrame(data).set_index("Segment")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    seg_colors = [TEAL, TEAL2, AMBER, GREEN, RED]

    # Left: % Revenue vs % Customers
    x = np.arange(len(df))
    w = 0.35
    axes[0].bar(x - w/2, df["% Revenue"],   width=w, color=TEAL,  label="% of Revenue",   zorder=3)
    axes[0].bar(x + w/2, df["% Customers"], width=w, color=AMBER, label="% of Customers", zorder=3)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(df.index, rotation=20, ha="right", fontsize=9)
    axes[0].set_title("Revenue vs Customer Share by Segment",
                      fontsize=12, fontweight="bold", color=NAVY, loc="left")
    axes[0].set_ylabel("%", fontsize=10, color=GRAY)
    axes[0].legend(fontsize=9, frameon=False)
    axes[0].yaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))

    # Right: Avg Revenue per segment
    axes[1].barh(df.index[::-1], df["Avg Revenue (£)"][::-1],
                 color=seg_colors[::-1], zorder=3)
    for i, (seg, val) in enumerate(zip(df.index[::-1], df["Avg Revenue (£)"][::-1])):
        axes[1].text(val + 150, i, f"£{val:,}", va="center", fontsize=9,
                     fontweight="bold", color=NAVY)
    axes[1].set_title("Avg Revenue per Customer by Segment",
                      fontsize=12, fontweight="bold", color=NAVY, loc="left")
    axes[1].set_xlabel("Average Revenue (£)", fontsize=10, color=GRAY)
    axes[1].set_xlim(0, 13500)
    axes[1].tick_params(axis="y", labelsize=9)
    axes[1].grid(axis="x")
    axes[1].grid(axis="y", visible=False)

    fig.suptitle("Customer Segment Comparison", fontsize=14,
                 fontweight="bold", color=NAVY, y=1.02)

    fig.add_artist(plt.Line2D([0, 1], [1, 1], transform=fig.transFigure,
                               color=TEAL, linewidth=4))

    plt.tight_layout()
    plt.savefig("chart3_segment_comparison.png", dpi=150, bbox_inches="tight")
    print("Saved: chart3_segment_comparison.png")
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
# HOW TO GENERATE FROM YOUR ACTUAL DATA
# ─────────────────────────────────────────────────────────────────────────────
def chart2_from_real_data(data_orders, data_customers):
    """
    Replace the hardcoded values in chart2_monthly_trend() with your real data.
    Call this after building data_orders and data_customers in your notebook.

    Parameters
    ----------
    data_orders   : DataFrame with columns [InvoiceDate, CustomerID]
    data_customers: DataFrame with columns [CustomerID, Segment]
    """
    data_orders = data_orders.copy()
    data_orders["Month"]     = pd.to_datetime(data_orders["InvoiceDate"]).dt.month
    data_orders["MonthName"] = pd.to_datetime(data_orders["InvoiceDate"]).dt.month_name()

    segmented = data_orders.merge(
        data_customers[["CustomerID", "Segment"]], on="CustomerID", how="left"
    )

    month_order = ["January","February","March","April","May","June",
                   "July","August","September","October","November","December"]

    pivot = (segmented
             .groupby(["MonthName", "Segment"])["InvoiceDate"]  # noqa: PD010
             .count()
             .unstack(fill_value=0)
             .reindex(month_order))

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = [TEAL, AMBER, GREEN, RED, TEAL2, GRAY]

    for i, seg in enumerate(pivot.columns):
        ax.plot(pivot.index, pivot[seg], marker="o", linewidth=2.2,
                color=colors[i % len(colors)], label=seg, markersize=4)

    ax.set_title("Monthly Order Trend by Segment", fontsize=14,
                 fontweight="bold", color=NAVY, loc="left")
    ax.set_ylabel("Number of Orders", fontsize=10, color=GRAY)
    ax.tick_params(axis="x", labelsize=9, rotation=30)
    ax.legend(fontsize=9, frameon=False)
    plt.tight_layout()
    plt.savefig("chart2_monthly_trend_real.png", dpi=150, bbox_inches="tight")
    print("Saved: chart2_monthly_trend_real.png")
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    chart1_revenue_by_segment()
    chart2_monthly_trend()
    chart3_segment_comparison()
    print("\nAll 3 charts saved as PNG files in the current directory.")
