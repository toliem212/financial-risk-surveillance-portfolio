# Methodology

Tài liệu này mô tả phương pháp ở mức đủ để đánh giá tư duy nghiệp vụ và định lượng, nhưng không công khai implementation production.

## VaR và Expected Shortfall

VaR trả lời câu hỏi: **với một mức tin cậy và cửa sổ lịch sử xác định, ngưỡng lỗ nào hiếm khi bị vượt qua?** Expected Shortfall đi thêm một bước và đo mức lỗ trung bình trong phần đuôi đã vượt VaR.

Các kiểm soát quan trọng gồm độ dài chuỗi, missing/stale data, sign convention, horizon và nhất quán giữa P&L/risk factor return.

## PV01 / DV01 và KR01

PV01 đo thay đổi giá trị khi lợi suất dịch chuyển **1 basis point**. Ở mức trực quan:

```text
PV01 ≈ - Modified Duration × Market Value × 0.0001
```

KR01/KRD phân rã độ nhạy theo từng điểm kỳ hạn để tránh che giấu rủi ro khi tổng duration có vẻ trung hòa nhưng đường cong chịu tác động không đồng đều.

## Stress testing

Stress testing được xem như lớp bổ sung cho VaR, đặc biệt với các biến động lớn, phi tuyến hoặc cấu trúc tương quan thay đổi. Kịch bản có thể gồm parallel shift, steepener/flattener, FX shock, spread widening và kết hợp nhiều risk factor.

## Liquidity / ALM

Các lớp phân tích chính:

- contractual và behavioural liquidity GAP;
- liquidity buffer và tài sản có thể huy động;
- funding concentration;
- survival horizon;
- LCR/NSFR tham chiếu;
- contingency funding và collateral/Repo–OMO.

## IRRBB

IRRBB được nhìn qua hai góc độ bổ sung:

- **ΔEVE**: thay đổi giá trị kinh tế của vốn khi đường cong lãi suất dịch chuyển;
- **ΔNII**: thay đổi thu nhập lãi ròng trong kỳ hạn quản trị.

Các giả định hành vi phải được tách khỏi dữ liệu contractual và có khả năng giải thích.

## Limits / EWS

Limit utilisation được chuẩn hóa theo cùng một định nghĩa trước khi phân loại trạng thái. Cảnh báo sớm không chỉ nhìn breach hiện tại mà còn quan tâm tốc độ tiến gần ngưỡng, stress-to-limit và chất lượng dữ liệu đầu vào.
