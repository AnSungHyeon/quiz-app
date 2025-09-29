import streamlit as st

# -----------------------------
# 문제, 보기, 정답, 해설 정의
# -----------------------------
questions = [
    # 1주차 (10문제)
    {
        "week": 1,
        "question": "문제 1: 다음 R 코드의 실행 결과로 알맞은 것은?\nx <- c(4, 7, 2, 9, 5)\ny <- sort(x, decreasing = TRUE)\nprint(y[2])",
        "options": ["9", "7", "5", "4"],
        "answer": 1,
        "explanation": "내림차순 정렬 후 두 번째 값은 7입니다."
    },
    {
        "week": 1,
        "question": "문제 2: 벡터(vectors)에 대한 설명으로 옳은 것은?",
        "options": [
            "벡터는 다양한 자료형의 원소들을 동시에 포함할 수 있다.",
            "벡터는 2차원 이상의 구조를 가질 수 있다.",
            "벡터의 모든 원소는 동일한 자료형이어야 한다.",
            "벡터는 행렬(matrix)과 동일한 개념이다."
        ],
        "answer": 2,
        "explanation": "벡터는 한 가지 자료형의 원소만 가질 수 있습니다."
    },
    {
        "week": 1,
        "question": "문제 3: data.table 코드 DT2 <- DT[ , .(sum_val = sum(value)), by = id]의 기능은?",
        "options": [
            "id별로 value의 평균을 계산한다.",
            "id가 중복된 행을 제거한다.",
            "id별로 value의 합계를 계산한다.",
            "전체 데이터의 value 합계를 구한다."
        ],
        "answer": 2,
        "explanation": "by=id로 그룹핑 후 value 합계를 계산합니다."
    },
    {
        "week": 1,
        "question": "문제 4: 데이터웨어하우스(Data Warehouse)와 데이터마트(Data Mart)에 대한 설명으로 옳지 않은 것은?",
        "options": [
            "데이터웨어하우스는 조직 전체 데이터를 통합 저장한 시스템이다.",
            "데이터마트는 특정 부서나 목적에 맞춘 데이터 저장소이다.",
            "데이터마트는 데이터를 실시간으로 처리하는 OLTP 시스템의 역할을 한다.",
            "데이터웨어하우스는 주로 OLAP 기반 분석을 지원한다."
        ],
        "answer": 2,
        "explanation": "데이터마트는 OLTP 시스템이 아니라 특정 목적 분석용 저장소입니다."
    },
    {
        "week": 1,
        "question": "문제 5: iris 데이터에서 virginica 종의 Sepal.Width 사분위수를 계산할 때 기대되는 순서는?",
        "options": [
            "0.25 사분위수 < 0.5 중앙값 < 0.75 사분위수 순",
            "0.5 중앙값이 항상 0.25 사분위수와 같거나 더 적다",
            "0.25 사분위수가 0.75 사분위수보다 크다",
            "중앙값은 최대값과 같다"
        ],
        "answer": 0,
        "explanation": "사분위수는 0.25 < 0.5 < 0.75 순서로 증가합니다."
    },
    {
        "week": 1,
        "question": "문제 6: R 리스트(list)에 대한 특징으로 옳지 않은 것은?",
        "options": [
            "리스트는 서로 다른 자료형의 원소들을 포함할 수 있다.",
            "리스트는 또 다른 리스트를 원소로 포함할 수 있다.",
            "리스트의 모든 원소는 동일한 자료구조이어야 한다.",
            "리스트는 벡터, 행렬, 데이터프레임 등을 포함할 수 있다."
        ],
        "answer": 2,
        "explanation": "리스트는 서로 다른 자료 구조를 포함할 수 있으므로 동일 자료구조일 필요 없습니다."
    },
    {
        "week": 1,
        "question": "문제 7: R 코드 aggregate(score ~ group, data=df, FUN=mean) 실행 결과는?",
        "options": [
            "그룹별 score의 합계가 나타난다.",
            "그룹별 score의 평균이 나타난다.",
            "그룹별 score의 중앙값이 나타난다.",
            "전체 score 평균이 나타난다."
        ],
        "answer": 1,
        "explanation": "FUN=mean이므로 그룹별 평균이 계산됩니다."
    },
    {
        "week": 1,
        "question": "문제 8: sqldf 패키지 관련 설명으로 옳지 않은 것은?",
        "options": [
            "R 환경에서 SQL 쿼리를 직접 실행할 수 있다.",
            "데이터프레임을 SQL 테이블처럼 다룰 수 있다.",
            "대용량 데이터 처리 시 data.table보다 항상 빠르다.",
            "패키지 설치 후 library로 로드해야 사용 가능하다."
        ],
        "answer": 2,
        "explanation": "sqldf가 항상 data.table보다 빠른 것은 아닙니다."
    },
    {
        "week": 1,
        "question": "문제 9: R 코드 v <- rep(seq(1,3, by=1), each=2) 실행 결과는?",
        "options": ["1 2 3", "1 1 2 2 3 3", "1 2 3 1 2 3", "3 3 2 2 1 1"],
        "answer": 1,
        "explanation": "each=2이므로 각 값이 두 번 반복됩니다."
    },
    {
        "week": 1,
        "question": "문제 10: 요인(factor)에 대한 설명으로 옳은 것은?",
        "options": [
            "연속형 수치 데이터를 저장할 때 사용한다.",
            "범주형 데이터를 저장하며 levels 속성이 있다.",
            "요인 변수를 그대로 숫자로 계산하면 원래 값과 완전히 같다.",
            "요인은 리스트(list)의 한 종류이다."
        ],
        "answer": 1,
        "explanation": "요인은 범주형(categorical) 데이터를 저장하고 levels 속성이 있습니다."
    },

    # 2주차 (10문제, 기존 ADsP 문제)
    {
        "week": 2,
        "question": "문제 1 – 결측값 확인\n\nx <- c(1, 2, NA, 4, NA)\nis.na(x) 실행 결과?",
        "options": [
            "FALSE FALSE FALSE FALSE FALSE",
            "TRUE TRUE TRUE TRUE TRUE",
            "FALSE FALSE TRUE FALSE TRUE",
            "TRUE TRUE FALSE TRUE FALSE"
        ],
        "answer": 2,
        "explanation": "세 번째와 다섯 번째 값이 NA이므로 TRUE가 됩니다."
    },
    {
        "week": 2,
        "question": "문제 2 – 결측값 제거\n\n결측값 있는 행 제거 함수는?",
        "options": ["na.replace(df)", "na.omit(df)", "is.na(df)", "drop.na(df)"],
        "answer": 1,
        "explanation": "na.omit(df)는 NA가 있는 행 제거."
    },
    {
        "week": 2,
        "question": "문제 3 – 결측값 대치법\n\n결측값을 평균값으로 대체하는 방법은?",
        "options": ["절단(trimming)", "단순 대치(single imputation)", "다중 대치(multiple imputation)", "윈저라이징(winsorizing)"],
        "answer": 1,
        "explanation": "평균값 대체는 단순 대치법입니다."
    },
    {
        "week": 2,
        "question": "문제 4 – 이상값 판단\n\n기하평균 ± 2.5표준편차 범위 밖의 값은?",
        "options": ["정상값", "이상값(outlier)", "결측값(NA)", "모수(parameter)"],
        "answer": 1,
        "explanation": "범위를 벗어난 값은 이상값입니다."
    },
    {
        "week": 2,
        "question": "문제 5 – 이상값 처리\n\n극단값을 상한/하한으로 조정하는 방법은?",
        "options": ["절단(trimming)", "조정(winsorizing)", "삭제(omit)", "평균 대치"],
        "answer": 1,
        "explanation": "Winsorizing은 극단값을 상한/하한으로 조정."
    },
    {
        "week": 2,
        "question": "문제 6 – 모집단과 표본\n\n전국 10만 명 중 1,000명을 표본으로 조사 시 설명은?",
        "options": [
            "표본 평균은 모집단 모수이다.",
            "모집단은 전체, 표본은 일부이다.",
            "표본값은 모집단 통계량이다.",
            "모집단과 표본은 항상 동일하다."
        ],
        "answer": 1,
        "explanation": "모집단=전체, 표본=일부."
    },
    {
        "week": 2,
        "question": "문제 7 – 단순랜덤추출법\n\n모집단 1,000명 중 100명을 무작위로 뽑는 방법은?",
        "options": ["단순랜덤추출법", "계통추출법", "집락추출법", "층화추출법"],
        "answer": 0,
        "explanation": "단순랜덤추출은 모두 동일 확률로 선택."
    },
    {
        "week": 2,
        "question": "문제 8 – 계통추출법\n\n100명 중 n=10, K=10. 첫 번째 1번 선택 시 표본은?",
        "options": ["1,2,...,10", "1,11,21,...,91", "10,20,...,100", "임의 선택 불가"],
        "answer": 1,
        "explanation": "계통추출: 시작점 + 매 K번째."
    },
    {
        "week": 2,
        "question": "문제 9 – 집락추출법\n\n대도시 5개 구를 단위로 표본 추출 시 방법은?",
        "options": ["단순랜덤추출", "계통추출", "집락추출", "층화추출"],
        "answer": 2,
        "explanation": "집락추출법은 집락 단위로 표본 추출."
    },
    {
        "week": 2,
        "question": "문제 10 – 층화추출법\n\n성별·연령별 층을 나누고 각 층에서 표본을 뽑아 대표성을 확보하는 방법은?",
        "options": ["A. 단순랜덤추출", "B. 계통추출", "C. 집락추출", "D. 층화추출"],
        "answer": 3,
        "explanation": "층화추출(stratified sampling)은 층별로 표본을 뽑아 대표성을 확보합니다."
    }
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="주차별 문제 퀴즈", layout="wide")
st.title("📘 주차별 문제 선택 퀴즈")
st.write("사이드바에서 주차를 선택하고 문제를 풀어보세요.")

# 사이드바에서 주차 선택
weeks = sorted(list(set([q["week"] for q in questions])))
selected_week = st.sidebar.selectbox("주차 선택", weeks)

# 선택한 주차 문제 필터링
week_questions = [q for q in questions if q["week"] == selected_week]

user_answers = []

for idx, q in enumerate(week_questions):
    answer = st.radio("선택", q["options"], key=f"{selected_week}_{idx}")
    user_answers.append(answer)

# 제출 버튼
if st.button("✅ 제출"):
    score = 0
    st.write("---")
    st.header("결과 확인")
    
    for idx, q in enumerate(week_questions):
        correct = q["options"][q["answer"]]
        if user_answers[idx] == correct:
            st.success(f"문제 {idx+1}: 정답 ✅")
            score += 1
        else:
            st.error(f"문제 {idx+1}: 오답 ❌ (정답: {correct})")
        st.caption(f"해설: {q['explanation']}")
    
    st.write("---")
    st.subheader(f"최종 점수: {score} / {len(week_questions)}")
