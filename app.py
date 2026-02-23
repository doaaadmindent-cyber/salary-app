import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="centered")

# ==========================================
# 2. تصميم آمن جداً (لا يخفي أي أشرطة أساسية)
# ==========================================
st.markdown("""
<style>
/* إخفاء شعار Streamlit السفلي فقط لحماية الموقع */
footer {visibility: hidden;}

/* تصميم بطاقة الراتب لتكون أنيقة وباللغة العربية */
.salary-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;
    direction: rtl; /* اتجاه النص من اليمين لليسار داخل البطاقة فقط */
    text-align: right;
    font-family: 'Arial', sans-serif;
}
.salary-row { 
    display: flex; 
    justify-content: space-between; 
    padding: 10px 0; 
    border-bottom: 1px dashed #e2e8f0; 
}
.salary-total { 
    font-weight: bold; 
    color: #16a34a; 
    font-size: 1.3em; 
    padding-top: 15px; 
    margin-top: 10px;
    border-top: 2px solid #cbd5e1; 
    display: flex; 
    justify-content: space-between;
}
.salary-deduct { color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. شريط المدير المالي (سيكون ظاهراً ومستقراً الآن)
# ==========================================
with st.sidebar:
    st.title("🔒 لوحة الإدارة")
    password = st.text_input("أدخل كلمة المرور:", type="password")
    
    if password == "1234":
        st.success("✅ تم تسجيل الدخول")
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
st.markdown("<h3 style='text-align: center; color: #475569;'>جامعة ابن سينا للعلوم الطبية والص



