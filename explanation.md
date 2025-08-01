# EDA Summary

This document provides an overview of the Excel workbook `Case Study - Data & AI Engineer.xlsx`. The file contains eight sheets with sales and reference information. Column names originally in Chinese have been translated to English where appropriate.

## Table Overview

| Sheet Name | Contents |
| --- | --- |
| 说明 | Instructions and notes for using the workbook |
| 1.1 RX 目标市场 | RX target market sales records |
| 1.2 电子商务 目标市场 | E‑commerce target market sales |
| 1.3 Device | Device market sales |
| 1.4 Retail | Retail pharmacy sales |
| 1.5 CSO&DSO 广阔市场 | Broad market sales for CSO/DSO channels |
| 1.6 非目标市场 | Non‑target market sales |
| 4 产品 DIM | Product dimension reference table |

## Column Details and Examples

### 说明 (Notes)
Two columns provide instructions:
1. **Unnamed: 0** – description in Chinese, e.g. “表1.0 全量汇总报告” (Table 1.0 overall report).
2. **Unnamed: 1** – additional notes, e.g. “（2021年月度全量汇总报告）”.

### 1.1 RX 目标市场 (RX Target Market)
Example row:
```text
Region: RX_E
Sales Rep Position: E_MR_0032
Report Month: 6
ID: 490653390
Product Name: 柏西
```
Key columns include region, sales representative position, report month, ID, product name, quantity, order date, dealer information (province, city, code, name, attribute), customer province/city, mapped customer details, customer attribute, data type (e.g., “RX目标医院销售” meaning RX target hospital sales), remarks, and original customer name.

### 1.2 电子商务 目标市场 (E‑commerce Target Market)
Example row:
```text
Upstream Attribution: 京东
Report Month: 6
ID: 490767150
Product Name: 倍舒痕 15g
```
Columns capture whether the customer is high potential, order dates, upstream dealer details, customer location, mapped customer code/name, customer attribute (e‑commerce), data type (e‑commerce target sales), remarks, and original customer name.

### 1.3 Device
Example row:
```text
Region: Device_S
Sales Rep Position: D_MR_0022
Report Month: 6
ID: 490694933
Product Name: 倍舒痕 15g
```
Similar structure to the RX sheet, with columns for dealer and customer information. Also includes mapping to associated customers for device sales.

### 1.4 Retail
Example row:
```text
Region: Retail_N
Sales Rep Position: MCH_KAP_43
Report Month: 6
ID: 7557324
Product Name: 必利劲 30*3
```
Tracks retail pharmacy sales with dealer and customer info, including mapping to chain headquarters. Data type is “Retail目标药店/诊所销售” meaning retail target pharmacy/clinic sales.

### 1.5 CSO&DSO 广阔市场 (CSO/DSO Broad Market)
Example row:
```text
Region: DSO_E
Report Month: 6
ID: 490692165
Product Name: 希爱力 5mg*14
Project Name: 浙江英特药业有限责任公司Cialis
```
Records broad‑market sales via CSO/DSO channels with similar dealer and customer columns. Includes a project name field.

### 1.6 非目标市场 (Non‑target Market)
Example row:
```text
Report Month: 6
ID: 490653393
Product Name: 开思亭 10*10
Original Customer: 永嘉县中医医院(永嘉县三江街道社区卫生服务中心)(集团)
```
Data structure mirrors the other sales sheets but represents non‑target channels (“RX非目标市场销售”).

### 4 产品 DIM (Product Dimension)
Reference list of products.
Example row:
```text
Brand: Asacol
Product Name: 安萨科 Asacol 800mg*30
```

