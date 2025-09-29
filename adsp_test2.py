import streamlit as st

# -----------------------------
# 20문제 데이터 (1주차 + 2주차)
# -----------------------------
questions = [
    # 1주차 (10문제)
    {
        "week": 1,
        "question": "문제 1: 다음 R 코드의 실행 결과로 알맞은 것은?",
        "code": "x <- c(4, 7, 2, 9, 5)\ny <- sort(x, decreasing = TRUE)\nprint(y[2])",
        "options": ["9", "7", "5", "4"],
        "answer": 1,
        "explanation": "내림차순 정렬 후 두 번째 값은 7입니다."
    },
    {
        "week": 1,
        "question": "문제 2: 벡터(vectors)에 대한 설명으로 옳은 것은?",
        "code": None,
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
        "question": "문제 3: 다음 R 코드 조각의 기능 또는 역할로 옳은 것은?",
        "code": "library(data.table)\nDT <- data.table(id=c(1,2,3,2,1), value=c(10,20,30,40,50))\nDT2 <- DT[ , .(sum_val = sum(value)), by=id]",
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
        "code": None,
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
        "code": "iris_sub <- iris[iris$Species=='virginica', ]\nquantiles <- quantile(iris_sub$Sepal.Width, probs=c(0.25,0.5,0.75))",
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
        "code": None,
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
        "code": "df <- data.frame(group=c('A','B','A','B'), score=c(80,90,70,85))\naggregate(score ~ group, data=df, FUN=mean)",
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
        "code": None,
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
        "code": "v <- rep(seq(1,3, by=1), each=2)\nprint(v)",
        "options": ["1 2 3", "1 1 2 2 3 3", "1 2 3 1 2 3", "3 3 2 2 1 1"],
        "answer": 1,
        "explanation": "each=2이므로 각 값이 두 번 반복됩니다."
    },
    {
        "week": 1,
        "question": "문제 10: 요인(factor)에 대한 설명으로 옳은 것은?",
        "code": None,
        "options": [
            "연속형 수치 데이터를 저장할 때 사용한다.",
            "범주형 데이터를 저장하며 levels 속성이 있다.",
            "요인 변수를 그대로 숫자로 계산하면 원래 값과 완전히 같다.",
            "요인은 리스트(list)의 한 종류이다."
        ],
        "answer": 1,
        "explanation": "요인은 범주형(categorical) 데이터를 저장하고 levels 속성이 있습니다."
    },

    # 2주차 (10문제)
    {
        "week": 2,
        "question": "문제 1 – 결측값 확인",
        "code": "x <- c(1, 2, NA, 4, NA)\nis.na(x)",
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
        "question": "문제 2 – 결측값 제거",
        "code": "df <- data.frame(a=c(1, NA, 3), b=c(4, 5, NA))\nna.omit(df)",
        "options": ["na.replace(df)", "na.omit(df)", "is.na(df)", "drop.na(df)"],
        "answer": 1,
        "explanation": "na.omit(df)는 NA가 있는 행 제거."
    },
    {
        "week": 2,
        "question": "문제 3 – 결측값 대치법",
        "code": None,
        "options": ["절단(trimming)", "단순 대치(single imputation)", "다중 대치(multiple imputation)", "윈저라이징(winsorizing)"],
        "answer": 1,
        "explanation": "평균값 대체는 단순 대치법입니다."
    },
    {
        "week": 2,
        "question": "문제 4 – 이상값 판단",
        "code": None,
        "options": ["정상값", "이상값(outlier)", "결측값(NA)", "모수(parameter)"],
        "answer": 1,
        "explanation": "범위를 벗어난 값은 이상값입니다."
    },
    {
        "week": 2,
        "question": "문제 5 – 이상값 처리",
        "code": None,
        "options": ["절단(trimming)", "조정(winsorizing)", "삭제(omit)", "평균 대치"],
        "answer": 1,
        "explanation": "Winsorizing은 극단값을 상한/하한으로 조정."
    },
    {
        "week": 2,
        "question": "문제 6 – 모집단과 표본",
        "code": None,
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
        "question": "문제 7 – 단순랜덤추출법",
        "code": None,
        "options": ["단순랜덤추출법", "계통추출법", "집락추출법", "층화추출법"],
        "answer": 0,
        "explanation": "단순랜덤추출은 모두 동일 확률로 선택."
    },
    {
        "week": 2,
        "question": "문제 8 – 계통추출법",
        "code": None,
        "options": ["1,2,...,10", "1,11,21,...,91", "10,20,...,100", "임의 선택 불가"],
        "answer": 1,
        "explanation": "계통추출: 시작점 + 매 K번째."
    },
    {
        "week": 2,
        "question": "문제 9 – 집락추출법",
        "code": None,
        "options": ["단순랜덤추출", "계통추출", "집락추출", "층화추출"],
        "answer": 2,
        "explanation": "집락추출법은 집락 단위로 표본 추출."
    },
    {
        "week": 2,
        "question": "문제 10 – 층화추출법",
        "code": None,
        "options": ["단순랜덤추출", "계통추출", "집락추출", "층화추출"],
        "answer": 3,
        "explanation": "층화추출(stratified sampling)은 층별로 표본을 뽑아 대표성을 확보합니다."
    }
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("ADsP 주차별 문제 풀이")

# 주차 선택
weeks = sorted(list(set([q["week"] for q in questions])))
week_choice = st.selectbox("주차를 선택하세요", weeks)

# 선택된 주차 문제 필터
week_questions = [q for q in questions if q["week"] == week_choice]

# 문제 출력
for idx, q in enumerate(week_questions):
    st.subheader(f"{idx+1}. {q['question']}")
    
    # R 코드 출력
    if q.get("code"):
        st.markdown("```r")
        st.markdown(q["code"])
        st.markdown("```")
    
    user_answer = st.radio("정답을 선택하세요", q["options"], key=f"{week_choice}_{idx}")
    
    if st.button("제출", key=f"submit_{week_choice}_{idx}"):
        if user_answer == q["options"][q["answer"]]:
            st.success("정답입니다!")
        else:
            st.error(f"오답입니다. 정답: {q['options'][q['answer']]}")
        st.info(f"해설: {q['explanation']}")
    st.write("---")
    st.subheader(f"최종 점수: {score} / {len(week_questions)}")
