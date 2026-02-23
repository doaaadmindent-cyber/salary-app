import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="centered")

# ==========================================
# 2. تصميم الواجهة وقسيمة الراتب
# ==========================================
st.markdown("""
<style>
/* إخفاء حقوق Streamlit بالأسفل */
footer {visibility: hidden;}

/* تصميم بطاقة الراتب لتكون أنيقة وباللغة العربية */
.salary-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;
    direction: rtl;
    text-align: right;
    font-family: 'Arial', sans-serif;
}
.salary-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px dashed #e2e8f0; }
.salary-total { font-weight: bold; color: #16a34a; font-size: 1.3em; padding-top: 15px; margin-top: 10px; border-top: 2px solid #cbd5e1; display: flex; justify-content: space-between;}
.salary-deduct { color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. العناوين الرئيسية
# ==========================================
st.markdown("<h1 style='text-align: center;'>نظام الرواتب الإلكتروني</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 4. لوحة الإدارة (بدون شريط جانبي - صندوق منسدل ذكي)
# ==========================================
# سيظهر هذا كزر أو صندوق مغلق، يفتحه المدير فقط لرفع الملف
with st.expander("🔒 لوحة الإدارة (اضغط هنا لرفع ملف الإكسل)"):
    password = st.text_input("أدخل كلمة المرور الخاصة بالمدير:", type="password")
    
    if password == "1234":
        st.success("✅ تم تسجيل الدخول بنجاح")
        uploaded_file = st.file_uploader("📥 ارفع ملف الإكسل للرواتب:", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث بيانات الرواتب بنجاح! يمكن للموظفين الآن البحث عن رواتبهم.")
    elif password != "":
        st.error("❌ كلمة المرور غير صحيحة")

st.write("---")

# ==========================================
# 5. واجهة الموظفين (البحث عن الراتب)
# ==========================================
emp_name = st.text_input("📝 يرجى إدخال اسمك الرباعي أو اللقب للبحث:")

if st.button("🔍 عرض الراتب"):
    if emp_name:
        try:
            df = pd.read_excel("salaries.xlsx")
            df['الاسم'] = df['الاسم'].astype(str).str.strip()
            user_data = df[df['الاسم'].str.contains(emp_name.strip(), na=False)]
            
            if not user_data.empty:
                row = user_data.iloc[0]
                
                st.markdown(f"""
                <div class="salary-card">
                    <h3 style="color: #2563eb; margin-bottom: 20px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
                        👤 بيانات الموظف: {row['الاسم']}
                    </h3>
                    
                    <div class="salary-row"><span><strong>{row['المنصب']}</strong></span><span>المنصب:</span></div>
                    <div class="salary-row"><span><strong>{row['اللقب العلمي']}</strong></span><span>اللقب العلمي:</span></div>
                    
                    <h4 style='color: #0ea5e9; margin-top: 20px;'>💰 الاستحقاقات</h4>
                    <div class="salary-row"><span><strong>{row['الراتب الاسمي']} د.ع</strong></span><span>الراتب الاسمي:</span></div>
                    <div class="salary-row"><span><strong>{row['الخدمة الجامعية']} د.ع</strong></span><span>الخدمة الجامعية:</span></div>
                    <div class="salary-row"><span><strong>{row['النقل']} د.ع</strong></span><span>مخصصات النقل:</span></div>
                    <div class="salary-row"><span><strong>{row['الزوجية']} د.ع</strong></span><span>المخصصات الزوجية:</span></div>
                    <div class="salary-row" style='background-color:#f0fdf4; padding: 10px;'>
                        <span><strong>{row['الراتب الكامل']} د.ع</strong></span>
                        <span><strong>الراتب الكامل (الإجمالي):</strong></span>
                    </div>
                    
                    <h4 style='color: #dc2626; margin-top: 20px;'>📉 الاستقطاعات</h4>
                    <div class="salary-row salary-deduct"><span><strong>{row['التقاعد']} د.ع</strong></span><span>التقاعد:</span></div>
                    <div class="salary-row salary-deduct"><span><strong>{row['الضريبة']} د.ع</strong></span><span>الضريبة:</span></div>
                    
                    <div class="salary-total">
                        <span>{row['الراتب الصافي بعد الاستقطاعات']} د.ع</span>
                        <span>الراتب الصافي (بعد الاستقطاعات):</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error("❌ عذراً، لم يتم العثور على اسم مطابق. يرجى التأكد من كتابة الاسم بشكل صحيح.")
                
        except FileNotFoundError:
            st.error("⚠️ لم يتم رفع ملف الرواتب من قبل الإدارة بعد. يرجى من المدير رفع الملف من القائمة أعلاه.")
        except Exception as e:
            st.error(f"⚠️ يوجد خطأ في قراءة بيانات الإكسل، تأكد من مطابقة أسماء الأعمدة. (التفاصيل: {e})")
    else:
        st.warning("⚠️ الرجاء إدخال الاسم أولاً.")


