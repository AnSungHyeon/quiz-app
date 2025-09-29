import streamlit as st

# -----------------------------
# 문제, 보기, 정답, 해설 정의
# -----------------------------
questions = [
    {
        "question": "문제 1 – 결측값 확인\n\nR 코드 실행 결과로 올바른 것은?\n\nx <- c(1, 2, NA, 4, NA)\nis.na(x)",
        "options": [
            "A. FALSE FALSE FALSE FALSE FALSE",
            "B. TRUE TRUE TRUE TRUE TRUE",
            "C. FALSE FALSE TRUE FALSE TRUE",
            "D. TRUE TRUE FALSE TRUE FALSE"
        ],
        "answer": 2,
        "explanation": "세 번째와 다섯 번째 값이 NA이므로 TRUE가 됩니다 → FALSE FALSE TRUE FALSE TRUE."
    },
    {
        "question": "문제 2 – 결측값 제거\n\n결측값이 포함된 데이터프레임 df에서 결측값 있는 행을 제거하는 함수는?",
        "options": ["A. na.replace(df)", "B. na.omit(df)", "C. is.na(df)", "D. drop.na(df)"],
        "answer": 1,
        "explanation": "na.omit(df)는 NA가 포함된 행 전체를 제거합니다."
    },
    {
        "question": "문제 3 – 결측값 대치법\n\n결측값을 해당 변수의 평균값으로 대체하는 방법은?",
        "options": ["A. 절단(trimming)", "B. 단순 대치(single imputation)", "C. 다중 대치(multiple imputation)", "D. 윈저라이징(winsorizing)"],
        "answer": 1,
        "explanation": "평균값으로 대체하는 것은 단순 대치(single imputation)입니다."
    },
    {
        "question": "문제 4 – 이상값 판단\n\n데이터가 기하평균 ± 2.5표준편차 범위를 벗어나면 어떻게 분류되는가?",
        "options": ["A. 정상값", "B. 이상값(outlier)", "C. 결측값(NA)", "D. 모수(parameter)"],
        "answer": 1,
        "explanation": "범위를 벗어난 값은 이상값(outlier)으로 판단합니다."
    },
    {
        "question": "문제 5 – 이상값 처리 방법\n\n극단값을 상한값이나 하한값으로 조정하여 분석에 포함시키는 방법은?",
        "options": ["A. 절단(trimming)", "B. 조정(winsorizing)", "C. 삭제(omit)", "D. 평균 대치"],
        "answer": 1,
        "explanation": "Winsorizing(조정)은 이상값을 상한 또는 하한으로 바꿔 포함시키는 방법입니다."
    },
    {
        "question": "문제 6 – 모집단과 표본\n\n전국 초등학생 10만 명 중 1,000명을 뽑아 설문을 진행했다. 올바른 설명은?",
        "options": [
            "A. 표본에서 계산한 평균은 모집단 모수이다.",
            "B. 모집단은 연구대상 전체, 표본은 일부이다.",
            "C. 표본에서 계산한 값은 모집단의 통계량이다.",
            "D. 모집단과 표본은 항상 동일하다."
        ],
        "answer": 1,
        "explanation": "모집단은 전체(10만 명), 표본은 일부(1천 명)입니다."
    },
    {
        "question": "문제 7 – 단순랜덤추출법\n\n모집단 1,000명 중 100명을 무작위로 뽑는 방법은?",
        "options": ["A. 단순랜덤추출법", "B. 계통추출법", "C. 집락추출법", "D. 층화추출법"],
        "answer": 0,
        "explanation": "단순랜덤추출법은 모든 개체가 동일한 확률로 뽑히는 방법입니다."
    },
    {
        "question": "문제 8 – 계통추출법\n\n100명 모집단에서 n=10명, K=10. 첫 번째로 1번을 뽑았다면 표본은?",
        "options": ["A. 1, 2, 3, …, 10", "B. 1, 11, 21, …, 91", "C. 10, 20, 30, …, 100", "D. 임의 선택 불가"],
        "answer": 1,
        "explanation": "계통추출은 시작점(1번)부터 매 K=10번째마다 선택 → 1, 11, 21, …, 91."
    },
    {
        "question": "문제 9 – 집락추출법\n\n대도시 5개 구를 집락으로 나누고, 구 단위로 표본을 추출하는 방법은?",
        "options": ["A. 단순랜덤추출", "B. 계통추출", "C. 집락추출", "D. 층화추출"],
        "answer": 2,
        "explanation": "집락추출법(cluster sampling)은 모집단을 집락 단위로 나누어 추출합니다."
    },
    {
        "question": "문제 10 – 층화추출법\n\n성별·연령별 층을 나누고 각 층에서 표본을 뽑아 대표성을 확보하는 방법은?",
        "options": ["A. 단순랜덤추출", "B. 계통추출", "C. 집락추출", "D. 층화추출"],
        "answer": 3,
        "explanation": "층화추출(stratified sampling)은 층별로 표본을 뽑아 대표성을 확보합니다."
    }
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="ADsP 연습문제 퀴즈", layout="wide")
st.title("📘 ADsP 연습문제 퀴즈 (10문제)")
st.write("아래 문제를 풀고, 제출 버튼을 눌러 점수를 확인하세요.")

# 사용자 답 저장
user_answers = []

# 문제 출력
for idx, q in enumerate(questions):
    st.subheader(q["question"])
    answer = st.radio(
        f"문제 {idx+1} 선택",
        q["options"],
        key=f"q{idx}"
    )
    user_answers.append(answer)

# 제출 버튼
if st.button("✅ 제출하기"):
    score = 0
    st.write("---")
    st.header("결과 확인")
    
    for idx, q in enumerate(questions):
        selected = user_answers[idx]
        correct = q["options"][q["answer"]]
        
        if selected == correct:
            st.success(f"문제 {idx+1}: 정답 ✅ ({selected})")
            score += 1
        else:
            st.error(f"문제 {idx+1}: 오답 ❌ (선택: {selected}, 정답: {correct})")
        
        st.caption(f"해설: {q['explanation']}")
    
    st.write("---")
    st.subheader(f"최종 점수: {score} / {len(questions)}")
