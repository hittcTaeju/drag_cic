import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, f1_score

# 1. 모델 불러오기
model = joblib.load('rf_model.pkl')

# 2. 테스트 데이터 로드
df = pd.read_csv('../../Desktop/df_sampled.csv')

# 3. 필요시 전처리 (특징 선택 또는 결측값 처리 등)
col_list =['Bwd Packet Length Max', 'Total Length of Fwd Packets',
           'Destination Port', 'Fwd Packet Length Max', 'Flow Packets/s',
           'Init_Win_bytes_forward', 'Fwd Packet Length Mean', 'Bwd Packets/s',
           'Flow IAT Std', 'Fwd Header Length', 'Init_Win_bytes_backward',
           'Flow IAT Mean', 'Total Fwd Packets']

# X 데이터: 예측에 사용할 피처들만 선택
X_test = df[col_list]

# y 데이터: 실제 타겟 변수 
y_test = df['Attack Type']  

# 4. 예측 수행
predictions = model.predict(X_test)

# 5. 예측 결과 저장
df['predictions'] = predictions
df.to_csv('predicted_output.csv', index=False)

# 6. 정확도와 F1 스코어 계산
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')  # 클래스 불균형이 있는 경우 weighted F1 스코어 사용

# 7. 결과 출력
print(f"예측이 완료되었습니다. 결과는 'predicted_output.csv' 파일에 저장되었습니다.")
print(f"정확도(Accuracy): {accuracy}")
print(f"F1 스코어: {f1}")

