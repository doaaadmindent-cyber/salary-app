import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="wide")

# ==========================================
# 2. إخفاء حقوق المنصة وتنسيق اللغة العربية
# ==========================================
st.markdown("""
<style>
footer {visibility: hidden;}

/* توجيه الواجهة بالكامل من اليمين لليسار */
.stApp {
    direction: rtl;
    font-family: 'Arial', sans-serif;
}

/* توجيه الجداول الأصلية لتبدأ من اليمين */
[data-testid="stTable"] {
    direction: rtl;
    text-align: right;
}
th {
    text-align: right !important;
    background-color: #f1f5f9 !important;
    color: #1e293b !important;
    font-size: 16px !important;
}
td {
    text-align: right !important;
    font-size: 15px !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. العناوين الرئيسية
# ==========================================
st.markdown("<h1 style='text-align: center;'>نظام الرواتب الإلكتروني</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 4. لوحة الإدارة (صندوق منسدل)
# ==========================================
with st.expander("🔒 لوحة الإدارة (اضغط هنا لرفع ملف الإكسل)"):
    password = st.text_input("أدخل كلمة المرور الخاصة بالمدير:", type="password")
    
    if password == "1234":
        st.success("✅ تم تسجيل الدخول بنجاح")
        uploaded_file = st.file_uploader("📥 ارفع ملف الإكسل للرواتب:", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث بيانات الرواتب بنجاح!")
    elif password != "":
        st.error("❌ كلمة المرور غير صحيحة")

st.write("---")

# ==========================================
# 5. واجهة الموظفين (البحث وعرض الجدول الأفقي)
# ==========================================
emp_name = st.text_input("📝 يرجى إدخال اسمك الرباعي أو اللقب للبحث:")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    search_button = st.button("🔍 عرض الراتب", use_container_width=True)

if search_button:
    if emp_name:
        try:
            df = pd.read_excel("salaries.xlsx")
            df['الاسم'] = df['الاسم'].astype(str).str.strip()
            user_data = df[df['الاسم'].str.contains(emp_name.strip(), na=False)]
            
            if not user_data.empty:
                # أخذ الصف الأول فقط في حال تشابه الأسماء
                employee_row = user_data.head(1)
                
                # ترتيب الأعمدة لتظهر في الجدول الأفقي بترتيب منطقي
                columns_order = [
                    'الاسم', 'المنصب', 'اللقب العلمي', 
                    'الراتب الاسمي', 'الخدمة الجامعية', 'النقل', 'الزوجية', 'الراتب الكامل', 
                    'التقاعد', 'الضريبة', 'الراتب الصافي بعد الاستقطاعات'
                ]
                
                # فلترة الأعمدة الموجودة فعلياً في ملف الإكسل لتجنب الأخطاء
                available_columns = [col for col in columns_order if col in employee_row.columns]
                final_data = employee_row[available_columns]
                
                st.success(f"✅ تفاصيل راتب الموظف: {employee_row['الاسم'].values[0]}")
                
                # عرض البيانات باستخدام جدول Streamlit الأصلي (أفقي 100%)
                st.table(final_data)
                
            else:
                st.error("❌ عذراً، لم يتم العثور على اسم مطابق. يرجى التأكد من كتابة الاسم بشكل صحيح.")
                
        except FileNotFoundError:
            st.error("⚠️ لم يتم رفع ملف الرواتب من قبل الإدارة بعد.")
        except Exception as e:
            st.error(f"⚠️ يوجد خطأ في قراءة بيانات الإكسل. تأكد من مطابقة أسماء الأعمدة. (التفاصيل: {e})")
    else:
        st.warning("⚠️ الرجاء إدخال الاسم أولاً.")
