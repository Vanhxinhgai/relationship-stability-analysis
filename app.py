import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.set_page_config(
    page_title="Relationship Stability Predictor",
    layout="wide"
)

st.title("Relationship Stability Analysis & Prediction")
st.write(
    "Prototype ứng dụng dự đoán trạng thái mối quan hệ "
    "dựa trên dữ liệu khảo sát."
)

# Load dataset
df = pd.read_csv("divorce_data.csv", sep=";")
df = df.drop_duplicates()

X = df.drop("Divorce", axis=1)
y = df["Divorce"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

st.subheader("Nhập câu trả lời khảo sát")

st.write("Mỗi câu được chấm từ 0 đến 4:")
st.write("0 = Không bao giờ, 1 = Hiếm khi, 2 = Thỉnh thoảng, 3 = Thường xuyên, 4 = Luôn luôn")

responses = {}

# Load question descriptions
ref = pd.read_csv("reference.tsv", sep="|")
ref["question_id"] = "Q" + ref["atribute_id"].astype(str)
question_map = dict(zip(ref["question_id"], ref["description"]))

responses = {}

for col in X.columns:
    question_text = question_map.get(col, col)
    responses[col] = st.slider(
        f"{col}: {question_text}",
        0, 4, 2
    )

input_data = pd.DataFrame([responses])

if st.button("Analyze / Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Kết quả dự đoán")

    if prediction == 0:
        st.success("Predicted Status: Stable / No Divorce")
    else:
        st.warning("Predicted Status: Divorce / Unstable")

    st.write(f"Probability of Stable / No Divorce: {probability[0]:.2%}")
    st.write(f"Probability of Divorce / Unstable: {probability[1]:.2%}")

    st.subheader("Lưu ý")
    st.write(
        "Kết quả chỉ mang tính tham khảo dựa trên dataset huấn luyện, "
        "không thay thế đánh giá của chuyên gia tâm lý hoặc tư vấn quan hệ."
    )