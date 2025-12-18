# MealX — Meal Delivery Analysis

SQL-backed analysis of a meal delivery service: operations, efficiency, promotions, and scaling.

---

## Contents

| File | Role |
|------|------|
| `data_cleaning.sql` | Clean and prepare the dataset |
| `exploratory_analysis.sql` | Demand, center performance, promotional impact |
| `dashboard_screenshot.png` | Excel dashboard snapshot |

---

## Insights

- **Rice Bowls** lead on revenue (one meal > ₦2.4B). **Beverages** drive highest total revenue from volume.
- **Promotions** lifted weekly orders ~3×; unregulated discounts suggest revenue leakage → need targeted, margin-aware campaigns.
- **Center Type A** is most scalable: high volume, coverage, and efficiency.
- **Order spikes** in Weeks 5, 48, 53, 60 → seasonal or event-driven; use for forecasting and promo planning.
- **Italian** and **Beverages** hold strong appeal → balance flagship items with volume drivers.

---

## Dashboard

![Excel Dashboard](dashboard_screenshot.png)

---

## Data limitations

1. **No year in weekly data** — week IDs span 145+ values but no year; limits cross-year trends and seasonality.
2. **No cost or margin per meal** — no unit cost, waste, or profit; limits promotion and profitability analysis.
3. **No delivery timing** — no dispatch/delivery timestamps; limits logistics and satisfaction analysis.

---

## Stack

- **SQL** — Cleaning and analysis  
- **Excel** — Dashboard and visuals

---

## Support

If you find this useful, consider starring the repo.
