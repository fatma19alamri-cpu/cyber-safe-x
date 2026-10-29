import streamlit as st
import random
from datetime import datetime

# =========================================================
# CyberSafe X
# منصة تفاعلية للسلامة الرقمية والأمن السيبراني
# =========================================================

st.set_page_config(
    page_title="CyberSafe X",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# التصميم
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #12304a 0%, transparent 30%),
        radial-gradient(circle at 90% 20%, #132b43 0%, transparent 25%),
        linear-gradient(135deg, #030812, #071523, #02060d);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 35px;
    border-radius: 28px;
    background:
        linear-gradient(
            135deg,
            rgba(15, 48, 72, 0.95),
            rgba(6, 18, 32, 0.95)
        );
    border: 1px solid rgba(103, 232, 249, 0.22);
    box-shadow: 0 20px 70px rgba(0,0,0,0.35);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.glow {
    color: #67e8f9;
    font-weight: 800;
}

.card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(10, 27, 43, 0.92);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 35px rgba(0,0,0,0.18);
    margin-bottom: 15px;
}

.feature-card {
    min-height: 190px;
}

.badge {
    display: inline-block;
    padding: 6px 13px;
    border-radius: 999px;
    background: rgba(103,232,249,0.12);
    color: #67e8f9;
    border: 1px solid rgba(103,232,249,0.25);
    margin: 3px;
}

.big-number {
    font-size: 2.5rem;
    font-weight: 800;
    color: #67e8f9;
}

.small-text {
    opacity: 0.72;
}

.danger-box {
    padding: 20px;
    border-radius: 18px;
    background: rgba(100, 20, 30, 0.22);
    border: 1px solid rgba(255,80,100,0.25);
}

.safe-box {
    padding: 20px;
    border-radius: 18px;
    background: rgba(10, 80, 70, 0.20);
    border: 1px solid rgba(80,220,190,0.25);
}

.info-box {
    padding: 20px;
    border-radius: 18px;
    background: rgba(20, 55, 90, 0.30);
    border: 1px solid rgba(100,180,255,0.20);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# بيانات الجلسة
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "xp" not in st.session_state:
    st.session_state.xp = 120

if "score" not in st.session_state:
    st.session_state.score = 0

if "completed" not in st.session_state:
    st.session_state.completed = []

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "phishing_finished" not in st.session_state:
    st.session_state.phishing_finished = False

if "footprint_finished" not in st.session_state:
    st.session_state.footprint_finished = False


# =========================================================
# الوظائف
# =========================================================

def add_xp(amount):

    st.session_state.xp += amount


def complete_task(task):

    if task not in st.session_state.completed:
        st.session_state.completed.append(task)


def get_level():

    xp = st.session_state.xp

    if xp < 200:
        return "🟢 مبتدئة"

    elif xp < 400:
        return "🔵 مستكشفة الأمن"

    elif xp < 700:
        return "🟣 حارسة رقمية"

    else:
        return "🟡 خبيرة CyberSafe"


def get_risk(score):

    if score >= 85:
        return "منخفض جدًا"

    elif score >= 70:
        return "منخفض"

    elif score >= 50:
        return "متوسط"

    else:
        return "مرتفع"


# =========================================================
# الأسئلة
# =========================================================

quiz_questions = [

    {
        "question":
        "وصلتك رسالة تقول إن حسابك سيتوقف خلال 10 دقائق. ما التصرف الأفضل؟",

        "answers": [
            "أضغط على الرابط بسرعة",
            "أرسل الرسالة لصديقتي",
            "أتحقق من المصدر وأدخل للموقع الرسمي بنفسي",
            "أرسل بياناتي حتى لا يتوقف الحساب"
        ],

        "correct": 2,

        "explanation":
        "الاستعجال والتهديد من أشهر أساليب التصيد الإلكتروني."
    },

    {
        "question":
        "ما أفضل طريقة للتعامل مع كلمات المرور؟",

        "answers": [
            "استخدام نفس كلمة المرور لكل الحسابات",
            "استخدام كلمة طويلة وفريدة لكل حساب مهم",
            "استخدام تاريخ الميلاد",
            "استخدام اسمك فقط"
        ],

        "correct": 1,

        "explanation":
        "كلمة مرور فريدة وطويلة تقلل خطر انتقال الاختراق بين الحسابات."
    },

    {
        "question":
        "تطبيق جديد يطلب الوصول إلى الميكروفون دون سبب واضح. ماذا تفعل؟",

        "answers": [
            "أوافق",
            "أعطيه جميع الصلاحيات",
            "أراجع سبب الصلاحية وأرفض غير الضرورية",
            "أرسل بياناتي للمطور"
        ],

        "correct": 2,

        "explanation":
        "من الأفضل منح التطبيقات أقل قدر من الصلاحيات اللازمة."
    },

    {
        "question":
        "وصلتك رسالة من حساب مجهول يطلب رمز التحقق OTP. ماذا تفعل؟",

        "answers": [
            "أرسل الرمز",
            "أرسل نصف الرمز",
            "لا أشارك الرمز",
            "أنشر الرمز في مجموعة"
        ],

        "correct": 2,

        "explanation":
        "رموز التحقق تعتبر معلومات حساسة ولا ينبغي مشاركتها مع الآخرين."
    },

    {
        "question":
        "ما فائدة المصادقة متعددة العوامل MFA؟",

        "answers": [
            "تجعل الإنترنت أسرع",
            "تضيف طبقة حماية إضافية للحساب",
            "تحذف الفيروسات",
            "تزيد مساحة الهاتف"
        ],

        "correct": 1,

        "explanation":
        "MFA تضيف عامل تحقق إضافيًا بجانب كلمة المرور."
    }

]


# =========================================================
# سيناريوهات التصيد
# =========================================================

phishing_scenarios = [

    {
        "title": "🚨 تنبيه أمني عاجل",

        "sender": "security-alert@example.invalid",

        "message":
        "تم اكتشاف نشاط غير معتاد على حسابك. يجب عليك التحقق خلال 10 دقائق حتى لا يتم إيقاف الحساب.",

        "clues": [
            "استخدام الخوف والاستعجال",
            "طلب اتخاذ إجراء سريع",
            "عنوان المرسل غير موثوق",
            "رسالة تهدف لدفع المستخدم لاتخاذ قرار سريع"
        ]
    },

    {
        "title": "🎁 مبروك! لقد فزت بجائزة",

        "sender": "winner@example.invalid",

        "message":
        "تهانينا! تم اختيارك للفوز بجائزة. أرسلي بياناتك الآن لاستلام الجائزة قبل انتهاء العرض.",

        "clues": [
            "جائزة غير متوقعة",
            "طلب معلومات شخصية",
            "استعجال المستخدم",
            "لا يوجد سبب واضح لاختيارك"
        ]
    },

    {
        "title": "🔐 تأكيد الحساب",

        "sender": "account-check@example.invalid",

        "message":
        "لأسباب أمنية نحتاج إلى تأكيد بيانات حسابك فورًا. لا تتجاهلي هذه الرسالة.",

        "clues": [
            "طلب معلومات الحساب",
            "ضغط نفسي",
            "رسالة غير متوقعة",
            "مصدر غير موثوق"
        ]
    }

]


# =========================================================
# القائمة الجانبية
# =========================================================

with st.sidebar:

    st.markdown("## 🛡️ CyberSafe X")

    st.caption(
        "منصة تفاعلية للسلامة الرقمية "
        "والوعي السيبراني"
    )

    st.divider()

    pages = {

        "🏠 لوحة القيادة": "home",

        "🧠 اختبار الوعي": "quiz",

        "🎣 مختبر التصيد": "phishing",

        "🧬 البصمة الرقمية": "footprint",

        "🚨 الطوارئ الرقمية": "emergency",

        "🤖 المدرب الذكي": "coach",

        "🏆 الإنجازات": "achievements"

    }

    for title, page_name in pages.items():

        if st.button(
            title,
            use_container_width=True
        ):

            st.session_state.page = page_name

            st.rerun()

    st.divider()

    st.markdown("### ⚡ مستواك")

    st.markdown(
        f"**{get_level()}**"
    )

    st.markdown(
        f"### {st.session_state.xp} XP"
    )

    progress = min(
        (st.session_state.xp % 500) / 500,
        1
    )

    st.progress(progress)

    st.caption(
        "لا نطلب كلمات المرور أو البيانات الحساسة."
    )


# =========================================================
# الصفحة الرئيسية
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">

        <span class="badge">
            🏆 مشروع ابتكاري 2026
        </span>

        <span class="badge">
            🛡️ Cybersecurity
        </span>

        <span class="badge">
            🤖 AI Education
        </span>

        <h1>
            🛡️ CyberSafe X
        </h1>

        <h2>
            درعك الرقمي يبدأ من وعيك
        </h2>

        <p>
            منصة تفاعلية تحول السلامة الرقمية
            من معلومات نظرية إلى تجربة
            يتعلم فيها المستخدم من قراراته
            ويكتشف نقاط الضعف في سلوكه الرقمي.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 مركز القيادة")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🧠 الوعي",
            f"{st.session_state.score}%"
        )

    with col2:

        st.metric(
            "⚡ XP",
            st.session_state.xp
        )

    with col3:

        st.metric(
            "🏆 المهام",
            len(st.session_state.completed)
        )

    with col4:

        st.metric(
            "🛡️ مستوى الخطر",
            get_risk(st.session_state.score)
        )

    st.markdown("## 🚀 ماذا يوجد داخل CyberSafe X؟")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card feature-card">

        <h2>🎣</h2>

        <h3>مختبر التصيد</h3>

        <p>
        تعلمي اكتشاف رسائل التصيد
        من خلال سيناريوهات تفاعلية.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card feature-card">

        <h2>🧬</h2>

        <h3>البصمة الرقمية</h3>

        <p>
        احصلي على مؤشر تعليمي
        لمستوى حمايتك الرقمية.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card feature-card">

        <h2>🤖</h2>

        <h3>المدرب الذكي</h3>

        <p>
        يحصل المستخدم على نصائح
        مختلفة حسب نتائجه.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("## ⚡ ابدئي رحلتك")

    if st.button(
        "🧠 ابدئي اختبار الوعي الآن",
        type="primary",
        use_container_width=True
    ):

        st.session_state.page = "quiz"

        st.rerun()


# =========================================================
# اختبار الوعي
# =========================================================

elif st.session_state.page == "quiz":

    st.title("🧠 اختبار الذكاء والوعي الرقمي")

    st.markdown("""
    <div class="info-box">

    هذا الاختبار لا يبحث عن إجابة مثالية فقط.

    الهدف هو معرفة طريقة تفكيرك عند مواجهة
    موقف رقمي مشبوه.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    answers_selected = 0

    correct_answers = 0

    for i, question in enumerate(quiz_questions):

        st.markdown(
            f"### السؤال {i + 1}"
        )

        st.write(
            question["question"]
        )

        answer = st.radio(
            "اختاري:",
            question["answers"],
            key=f"quiz_question_{i}",
            index=None
        )

        if answer is not None:

            answers_selected += 1

            selected_index = question["answers"].index(
                answer
            )

            if selected_index == question["correct"]:

                correct_answers += 1

    st.write("")

    if st.button(
        "🔍 تحليل النتيجة",
        type="primary",
        use_container_width=True,
        disabled=answers_selected != len(quiz_questions)
    ):

        final_score = round(
            (correct_answers / len(quiz_questions)) * 100
        )

        st.session_state.score = final_score

        st.session_state.quiz_finished = True

        add_xp(50)

        complete_task("quiz")

        st.divider()

        st.markdown("## 🎯 نتيجتك")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="card">

                <div class="big-number">
                {final_score}%
                </div>

                <p>مؤشر الوعي</p>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="card">

                <div class="big-number">
                {correct_answers}
                </div>

                <p>إجابات صحيحة</p>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="card">

                <div class="big-number">
                +50
                </div>

                <p>XP مكتسبة</p>

                </div>
                """,
                unsafe_allow_html=True
            )

        if final_score >= 85:

            st.success(
                "🏆 ممتاز! لديك مستوى قوي من الوعي الرقمي."
            )

        elif final_score >= 60:

            st.warning(
                "🔵 جيد! لديك أساس جيد ويمكن تحسين بعض المهارات."
            )

        else:

            st.error(
                "🟠 تحتاجين إلى تدريب إضافي على مواقف الأمن الرقمي."
            )

        st.info(
            "💡 نصيحة: انتقلي إلى مختبر التصيد لتختبري نفسك في مواقف عملية."
        )


# =========================================================
# مختبر التصيد
# =========================================================

elif st.session_state.page == "phishing":

    st.title("🎣 مختبر التصيد الإلكتروني")

    st.markdown("""
    <div class="danger-box">

    ⚠️ هذه محاكاة تعليمية آمنة.

    لا تدخلي أي كلمة مرور أو بيانات شخصية حقيقية.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    scenario = random.choice(
        phishing_scenarios
    )

    st.markdown(
        f"""
        <div class="card">

        <h2>{scenario["title"]}</h2>

        <p>
        <b>المرسل:</b>
        {scenario["sender"]}
        </p>

        <hr>

        <p>
        {scenario["message"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🤔 ماذا ستفعلين؟")

    decision = st.radio(
        "اختاري القرار:",
        [
            "أتعامل معها كرسالة مشبوهة وأتحقق من المصدر الرسمي",
            "أضغط على الرابط فورًا",
            "أرسل بياناتي حتى لا يتم إيقاف الحساب"
        ],
        index=None
    )

    if st.button(
        "🔎 حللي قراري",
        type="primary",
        use_container_width=True,
        disabled=decision is None
    ):

        if decision.startswith(
            "أتعامل معها"
        ):

            st.success(
                "🎯 قرار ممتاز! اكتشفتِ أن الرسالة تحتوي على إشارات خطر."
            )

            add_xp(75)

        else:

            st.error(
                "⚠️ هذا القرار قد يعرض الحساب للخطر."
            )

            add_xp(15)

        st.markdown(
            "### 🚩 إشارات الخطر"
        )

        for clue in scenario["clues"]:

            st.markdown(
                f"- 🚩 {clue}"
            )

        st.session_state.phishing_finished = True

        complete_task("phishing")


# =========================================================
# البصمة الرقمية
# =========================================================

elif st.session_state.page == "footprint":

    st.title("🧬 تحليل البصمة الرقمية")

    st.markdown("""
    <div class="info-box">

    هذا ليس فحصًا حقيقيًا لحساباتك.

    إنه تقييم تعليمي مبني على عاداتك الرقمية
    لمساعدتك على معرفة النقاط التي تحتاج إلى تحسين.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    risk_points = 0

    questions = [

        (
            "هل تستخدمين كلمة المرور نفسها في أكثر من حساب؟",
            [
                "نعم",
                "أحيانًا",
                "لا"
            ]
        ),

        (
            "هل تستخدمين المصادقة متعددة العوامل للحسابات المهمة؟",
            [
                "نعم في معظمها",
                "في بعضها",
                "لا"
            ]
        ),

        (
            "هل تراجعين صلاحيات التطبيقات؟",
            [
                "دائمًا",
                "أحيانًا",
                "نادراً"
            ]
        ),

        (
            "هل تنشرين معلومات شخصية بشكل علني؟",
            [
                "كثيرًا",
                "أحيانًا",
                "نادراً"
            ]
        ),

        (
            "هل تفتحين الروابط من مصادر مجهولة؟",
            [
                "نعم",
                "أحيانًا",
                "نادراً"
            ]
        )

    ]

    selected = 0

    for i, (question, options) in enumerate(questions):

        answer = st.radio(
            question,
            options,
            key=f"footprint_{i}",
            index=None
        )

        if answer is not None:

            selected += 1

            if answer in [
                "نعم",
                "كثيرًا",
                "نادراً"
            ]:

                risk_points += 2

            elif answer in [
                "أحيانًا",
                "في بعضها"
            ]:

                risk_points += 1

    if st.button(
        "🧬 إنشاء خريطة الحماية",
        type="primary",
        use_container_width=True,
        disabled=selected != len(questions)
    ):

        protection_score = max(
            0,
            100 - (risk_points * 10)
        )

        st.session_state.footprint_finished = True

        complete_task("footprint")

        add_xp(60)

        st.divider()

        st.markdown(
            "## 🧬 خريطة الحماية الرقمية"
        )

        st.progress(
            protection_score / 100
        )

        st.markdown(
            f"""
            <div class="card">

            <div class="big-number">
            {protection_score}%
            </div>

            <p>
            مؤشر الحماية الرقمية
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if protection_score >= 80:

            st.success(
                "🛡️ ممتاز! عاداتك الرقمية جيدة."
            )

        elif protection_score >= 60:

            st.warning(
                "🔵 جيد، لكن توجد بعض العادات التي يمكنك تحسينها."
            )

        else:

            st.error(
                "🚨 مستوى الخطر مرتفع نسبيًا. ابدئي بتقوية الحسابات المهمة."
            )


# =========================================================
# وضع الطوارئ
# =========================================================

elif st.session_state.page == "emergency":

    st.title("🚨 وضع الطوارئ الرقمية")

    st.markdown("""
    إذا شككتِ في تعرض حسابك لعملية تصيد أو اختراق،
    لا تتصرفي بسرعة عشوائية.

    اتبعي الخطوات العامة التالية:
    """)

    emergency_steps = [

        "لا تدخلي أي بيانات إضافية في الصفحة المشبوهة.",

        "غيّري كلمة المرور من التطبيق أو الموقع الرسمي.",

        "فعّلي المصادقة متعددة العوامل MFA.",

        "راجعي الأجهزة والجلسات المرتبطة بالحساب.",

        "تحققي من رسائل البريد والإشعارات الأمنية.",

        "احتفظي بلقطة للرسالة المشبوهة دون نشر بيانات حساسة.",

        "إذا كان الأمر يتعلق بحساب مالي، استخدمي قناة الجهة الرسمية المعروفة."
    ]

    for number, step in enumerate(
        emergency_steps,
        1
    ):

        st.markdown(
            f"""
            <div class="card">

            <h3>
            {number}️⃣
            </h3>

            <p>
            {step}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button(
        "✅ أكملت مراجعة خطوات الطوارئ",
        type="primary",
        use_container_width=True
    ):

        add_xp(40)

        complete_task("emergency")

        st.success(
            "تم تسجيل المهمة في رحلتك."
        )


# =========================================================
# المدرب الذكي
# =========================================================

elif st.session_state.page == "coach":

    st.title("🤖 CyberSafe AI Coach")

    st.markdown("""
    <div class="hero">

    <h2>
    مدربك الرقمي الشخصي
    </h2>

    <p>
    بدل إعطاء جميع المستخدمين النصائح نفسها،
    يختار المدرب مسار التدريب بناءً على نتائجك.
    </p>

    </div>
    """, unsafe_allow_html=True)

    score = st.session_state.score

    if not st.session_state.quiz_finished:

        st.info(
            "🧠 ابدئي باختبار الوعي أولًا حتى يستطيع المدرب بناء توصية مناسبة."
        )

        if st.button(
            "ابدئي الاختبار",
            type="primary"
        ):

            st.session_state.page = "quiz"

            st.rerun()

    else:

        st.markdown(
            f"### نتيجتك الحالية: {score}%"
        )

        if score < 50:

            st.error(
                "🚨 المدرب يقترح: ابدئي بأساسيات التصيد وكلمات المرور."
            )

            recommendation = """
            مسارك المقترح:

            1. مختبر التصيد
            2. اختبار الوعي مرة أخرى
            3. تحليل البصمة الرقمية
            """

        elif score < 80:

            st.warning(
                "🔵 المدرب يقترح: ركزي على التحقق من الرسائل والصلاحيات."
            )

            recommendation = """
            مسارك المقترح:

            1. مختبر التصيد
            2. تحليل البصمة الرقمية
            3. مراجعة وضع الطوارئ
            """

        else:

            st.success(
                "🏆 مستوى ممتاز! المدرب يقترح تحديات متقدمة."
            )

            recommendation = """
            مسارك المقترح:

            1. تحليل البصمة الرقمية
            2. مراجعة الطوارئ
            3. تحديات التصيد المتقدمة
            """

        st.markdown(
            f"""
            <div class="card">

            <h3>🎯 خطتك الشخصية</h3>

            <p>
            {recommendation}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## 💡 نصيحة اليوم")

    tips = [

        "لا تشاركي رمز OTP مع أي شخص.",

        "استخدمي كلمات مرور فريدة للحسابات المهمة.",

        "تحققي من عنوان الموقع قبل تسجيل الدخول.",

        "راجعي صلاحيات التطبيقات بشكل دوري.",

        "فعّلي MFA للحسابات المهمة.",

        "لا تسمحي للاستعجال أن يتخذ القرار بدلًا منك."

    ]

    st.info(
        random.choice(tips)
    )


# =========================================================
# الإنجازات
# =========================================================

elif st.session_state.page == "achievements":

    st.title("🏆 مركز الإنجازات")

    achievements = [

        (
            "🔰 البداية الآمنة",
            "أكملت أول مهمة.",
            len(st.session_state.completed) >= 1
        ),

        (
            "🧠 العقل السيبراني",
            "أكملت اختبار الوعي.",
            "quiz" in st.session_state.completed
        ),

        (
            "🎣 صيادة التصيد",
            "أكملت مختبر التصيد.",
            "phishing" in st.session_state.completed
        ),

        (
            "🧬 حارسة البصمة",
            "حللت البصمة الرقمية.",
            "footprint" in st.session_state.completed
        ),

        (
            "🚨 مستعدة للطوارئ",
            "راجعت خطوات الطوارئ.",
            "emergency" in st.session_state.completed
        ),

        (
            "⚡ 250 XP",
            "وصلت إلى 250 نقطة خبرة.",
            st.session_state.xp >= 250
        ),

        (
            "🏆 حارسة CyberSafe",
            "أكملت ثلاث مهام أو أكثر.",
            len(st.session_state.completed) >= 3
        )

    ]

    for title, description, unlocked in achievements:

        icon = "✅" if unlocked else "🔒"

        st.markdown(
            f"""
            <div class="card">

            <h3>
            {icon} {title}
            </h3>

            <p>
            {description}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# أسفل التطبيق
# =========================================================

st.divider()

st.caption(
    f"""
    🛡️ CyberSafe X |
    مشروع السلامة الرقمية |
    2026 |
    آخر تحديث: {datetime.now().strftime("%Y-%m-%d")}
    """
)