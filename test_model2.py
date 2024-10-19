import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, f1_score

# 1. 모델 불러오기
model = joblib.load('rf_model.pkl')

# 2. 테스트 데이터 로드
df = pd.read_csv('../../Desktop/flow.csv')

# 3. 필요시 전처리 (특징 선택 또는 결측값 처리 등)
col_list =['Bwd Packet Length Max', 'Total Length of Fwd Packets',
       'Destination Port', 'Fwd Packet Length Max', 'Flow Packets/s',
       'Init_Win_bytes_forward', 'Fwd Packet Length Mean', 'Bwd Packets/s',
       'Flow IAT Std', 'Fwd Header Length', 'Init_Win_bytes_backward',
       'Flow IAT Mean', 'Total Fwd Packets']
df= df[col_list]
# 4. 예측 수행
predictions = model.predict(df)

# 5. 예측 결과 출력 또는 저장
df['predictions'] = predictions
df.to_csv('predicted_output.csv', index=False)

print("예측이 완료되었습니다. 결과는 'predicted_output.csv' 파일에 저장되었습니다.")
