import pandas as pd


def preprocess_csv(input_filepath, output_filepath):
    # CSV 파일을 읽음
    df = pd.read_csv(input_filepath)

    # 예: 데이터 전처리 과정
    # (필요에 따라 데이터를 처리할 수 있음)
    df.fillna(0, inplace=True)  # 결측값을 0으로 채우기
    df['new_column'] = df['existing_column'] * 2  # 새로운 컬럼 추가 예시

    # 처리된 데이터프레임을 새로운 .csv 파일로 저장
    df.to_csv(output_filepath, index=False)

    return output_filepath
