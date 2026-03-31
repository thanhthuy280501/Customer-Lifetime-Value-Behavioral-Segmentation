# Online Retail: Customer Lifetime Value & Segmentation Analysis

A end-to-end Python data analysis project exploring 1M+ transactions from a UK-based online giftware retailer to identify customer segments, uncover revenue drivers, and generate actionable business recommendations.

---

## Project Overview

Most businesses treat every customer the same. This project proves they shouldn't.

By analyzing two years of transactional data (Dec 2009 – Dec 2011), this project identifies a specific **High Value** segment (~20% of customers) responsible for **77% of total revenue** — and builds a strategic roadmap for re-engaging at-risk customers, converting one-time buyers, and maximizing lifetime value across all segments.

---

## Business Questions

1. Which customer segments generate the most revenue, and how do they behave differently?
2. What is the "tipping point" for repeat purchases — how many days after the first purchase does loyalty drop?
3. Which products drive cross-selling behavior across segments?

---

## Dataset

| Field | Details |
|-------|---------|
| Source | [Online Retail II — Kaggle](https://www.kaggle.com/datasets/jillwang87/online-retail-ii) |
| Size | 1,067,371 rows across 2 years |
| Grain | One row = one line item per invoice |
| Columns | InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country |

---

## Tools & Skills

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **Data Cleaning** — anomaly detection, duplicate resolution, business-logic filtering
- **Feature Engineering** — RFM metrics (Recency, Frequency, Monetary), TotalRevenue, CancellationRate
- **Customer Segmentation** — rule-based segmentation using quantile thresholds
- **Data Visualization** — segment comparison charts, time behavior plots, annual trend lines

---

## Project Structure

```
retail-clv-segmentation/
│
├── Thuy_Nguyen_Retail_CLV_Analysis.ipynb   ← Main analysis notebook
└── README.md
```

---

## Key Findings

### Data Quality
- Removed **3,464 anomalous rows**: store corrections ($0 price + negative qty), bad debt adjustments (A-invoices), and one data error
- Resolved **34,335 exact duplicate rows** (3.22% of dataset)
- Retained **22.7% missing CustomerIDs** (guest checkouts) for product-level analysis

### Customer Segments

| Segment | % of Customers | % of Revenue | Avg Revenue | Avg Orders |
|---------|---------------|-------------|-------------|------------|
| High Value | 19.9% | 77.1% | £10,879 | 23 |
| Low Value | 49.3% | 16.4% | £934 | 4 |
| One-time Buyer | 23.5% | 2.5% | £297 | 1 |
| Frequent but Low Spend | 5.2% | 3.7% | £1,997 | 13 |
| Risky | 1.2% | 0.6% | £1,500 | 7 |

### Time Behavior
- **Peak days:** Tuesday – Thursday (all segments)
- **Peak hours:** 10 AM – 3 PM
- **Peak month:** November (holiday gifting season)
- January and February are consistently the slowest months

### Business Recommendations

| Segment | Strategy |
|---------|---------|
| High Value | VIP loyalty program, early product access, personalized cross-sells |
| Low Value | Bundle deals, free-shipping thresholds to increase average order value |
| One-time Buyer | Post-purchase email sequence with second-purchase discount |
| Frequent but Low Spend | Upsell to premium alternatives, subscription offers |
| Risky | Investigate cancellation root causes, improve product descriptions |

---

## How to Run

1. Clone this repository
```bash
git clone https://github.com/thanhthuy280501/retail-clv-segmentation.git
```

2. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/jillwang87/online-retail-ii) and place it in your Google Drive or local path

3. Open the notebook in Google Colab or Jupyter and update the file path in Section 1

4. Run all cells in order

---

## Author

**Thuy Nguyen**  
B.S. Computer Science, Minor in Data Analytics — University of Michigan-Flint  
[LinkedIn](https://www.linkedin.com/in/thanhthuy280501) · [GitHub](https://github.com/thanhthuy280501)
