import pandas as pd


def 정제(df):
    df = df.copy()
    print("시작:", len(df))

    # 1. 점수가 비어 있는 행 제거
    df = df.dropna(subset=["점수"])
    print("빈칸 제거:", len(df))

    # 2. 완전히 동일한 중복 행 제거
    df = df.drop_duplicates()
    print("중복 제거:", len(df))

    # 3. 반과 과목의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    print("공백 제거:", len(df))

    # 4. 0~100점 범위를 벗어난 행 제거
    df = df[df["점수"].between(0, 100)]
    print("범위 밖 제거:", len(df))

    return df


if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)

    print("반 종류:", sorted(df["반"].unique()))
    print("과목 종류:", sorted(df["과목"].unique()))
        # B. 필터링
    수학 = df[df["과목"] == "수학"]
    print("수학 데이터 개수:", len(수학))
        # C. 그룹화
    print("\n반별 평균:")
    print(df.groupby("반")["점수"].mean())

    print("\n과목별·반별 평균:")
    print(df.groupby(["과목", "반"])["점수"].mean())
        # D. 통계
    print("\n반별 통계:")
    print(df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]))
        # 분석 결과 검증
    print("\n그룹 합계:", df.groupby("반")["점수"].sum().sum())
    print("전체 합계:", df["점수"].sum())
    print("그룹 개수 합:", df.groupby("반")["점수"].count().sum())

    # 스팟 체크: 1반 수학
    print("\n1반 수학 점수:")
    print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"].tolist())
    # mini.csv 손계산 검증
mini = 정제(pd.read_csv("mini.csv"))

print("\nmini.csv 검증 결과")
print("정제 후 행 수:", len(mini))
print("반별 평균:")
print(mini.groupby("반")["점수"].mean())
def 반별평균(df):
    return df.groupby("반")["점수"].mean()