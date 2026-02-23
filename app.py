import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة (تم إضافة أمر فتح الشريط الجانبي تلقائياً)
# ==========================================
st.set_page_config(
    page_title="نظام الرواتب", 
    page_icon="💰", 
    layout="centered", 
    initial_sidebar_state="expanded" # هذا الأمر يجبر شريط المدير على الظهور
)

# ==========================================
# 2. كود التصميم الاحترافي (مصحح لتفادي اختفاء القوائم)
# ==========================================
st.markdown("""
<style>
/* توجيه النصوص فقط للغة العربية لتفادي كسر واجهة الموقع */
h1, h2, h3, p, span, label, input, div.stMarkdown {
    direction: rtl !important;
    text-align: right !important;
    font-family: 'Arial', sans-serif;
}

/* إخفاء قائمة Streamlit العلوية والفوتر لحماية النظام */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* خلفية احترافية متدرجة */
[data-testid="stAppViewContainer"] {
    background-color: #f4f6f9;
    background-image: linear-gradient(180deg, #e2e8f0 0%, #ffffff 100%);
}

/* تحسين شكل حقل الإدخال */
input[type="text"], input[type="password"] {
    background-color: #ffffff !important;
    border: 2px solid #cbd5e1 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05) !important;
}

/* ألوان العناوين */
h1, h2, h3 { color: #1e293b !important; }

/* تصميم بطاقة تفاصيل الراتب (منسقة لليمين) */
.salary-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;
    direction: rtl;
}
.salary-header { color: #2563eb; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 15px; }
.salary-row { display: flex; justify-content: space-between; flex-direction: row-reverse; padding: 5px 0; border-bottom: 1px dashed #f1f5f9; }
.salary-total { font-weight: bold; color: #16a34a; font-size: 1.2em; padding-top: 15px; border-top: 2px solid #e2e8f0; display: flex; justify-content: space-between; flex-direction: row-reverse;}
.salary-deduct { color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. شريط المدير المالي (القائمة الجانبية)
# ==========================================
with st.sidebar:
    st.markdown("<h2>🔒 لوحة تحكم الإدارة</h2>", unsafe_allow_html=True)
    password = st.text_input("أدخل كلمة المرور:", type="password")
    
    # كلمة مرور المدير هي 1234
    if password == "1234":
        st.success("✅ تم تسجيل الدخول بنجاح")
        uploaded_file = st.file_uploader("📥 ارفع ملف الإكسل للرواتب:", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث بيانات الرواتب بنجاح!")
    elif password != "":
        st.error("❌ كلمة المرور غير صحيحة")

# ==========================================
# 4. الواجهة الرئيسية (للموظفين)
# ==========================================
st.markdown("<h1 style='text-align: center;'>نظام الرواتب الإلكتروني</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569 !important;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>", unsafe_allow_html=True)
st.write("---")

# حقل البحث (بالاسم)
emp_name = st.text_input("📝 يرجى إدخال اسمك الرباعي أو اللقب للبحث:")

if st.button("🔍 عرض الراتب"):
    if emp_name:
        try:
            # قراءة ملف الإكسل
            df = pd.read_excel("salaries.xlsx")
            
            # تنظيف المسافات للبحث بدقة
            df['الاسم'] = df['الاسم'].astype(str).str.strip()
            
            # البحث عن الاسم
            user_data = df[df['الاسم'].str.contains(emp_name.strip(), na=False)]
            
            if not user_data.empty:
                row = user_data.iloc[0]
                
                # عرض التفاصيل داخل بطاقات HTML أنيقة
                st.markdown(f"""
                <div class="salary-card">
                    <h3 class="salary-header">👤 بيانات الموظف: {row['الاسم']}</h3>
                    <div class="salary-row"><span><strong>{row['المنصب']}</strong></span><span>:المنصب</span></div>
                    <div class="salary-row"><span><strong>{row['اللقب العلمي']}</strong></span><span>:اللقب العلمي</span></div>
                    
                    <h4 style='color: #0ea5e9; margin-top: 20px; text-align: right;'>💰 الاستحقاقات</h4>
                    <div class="salary-row"><span><strong>{row['الراتب الاسمي']} د.ع</strong></span><span>:الراتب الاسمي</span></div>
                    <div class="salary-row"><span><strong>{row['الخدمة الجامعية']} د.ع</strong></span><span>:الخدمة الجامعية</span></div>
                    <div class="salary-row"><span><strong>{row['النقل']} د.ع</strong></span><span>:مخصصات النقل</span></div>
                    <div class="salary-row"><span><strong>{row['الزوجية']} د.ع</strong></span><span>:المخصصات الزوجية</span></div>
                    <div class="salary-row" style='background-color:#f0fdf4;'><span><strong>{row['الراتب الكامل']} د.ع</strong></span><span>:<strong>الراتب الكامل (الإجمالي)</strong></span></div>
                    
                    <h4 style='color: #dc2626; margin-top: 20px; text-align: right;'>📉 الاستقطاعات</h4>
                    <div class="salary-row salary-deduct"><span><strong>{row['التقاعد']} د.ع</strong></span><span>:التقاعد</span></div>
                    <div class="salary-row salary-deduct"><span><strong>{row['الضريبة']} د.ع</strong></span><span>:الضريبة</span></div>
                    
                    <div class="salary-total">
                        <span>{row['الراتب الصافي بعد الاستقطاعات']} د.ع</span>
                        <span>:الراتب الصافي (بعد الاستقطاعات)</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error("❌ عذراً، لم يتم العثور على اسم مطابق. يرجى التأكد من كتابة الاسم بشكل صحيح.")
                
        except FileNotFoundError:
            st.error("⚠️ لم يتم رفع ملف الرواتب من قبل الإدارة (salaries.xlsx) حتى الآن.")
        except KeyError as e:
            st.error(f"⚠️ يوجد خطأ في أعمدة ملف الإكسل. الرجاء التأكد من وجود عمود باسم: {e}")
    else:
        st.warning("⚠️ الرجاء إدخال الاسم أولاً.")





