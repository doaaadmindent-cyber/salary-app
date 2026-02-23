import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية (دعم اللغة العربية)
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="centered")

# ==========================================
# 2. كود التصميم الاحترافي ودعم من اليمين لليسار (RTL)
# ==========================================
st.markdown("""
<style>
/* دعم اللغة العربية (من اليمين لليسار) وتغيير الخط */
* {
    direction: rtl;
    font-family: 'Arial', sans-serif;
}

/* إخفاء القوائم لحماية النظام */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] {background-color: transparent;}

/* خلفية احترافية */
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
    text-align: right !important;
}

/* ألوان العناوين */
h1, h2, h3 { color: #1e293b !important; }

/* تصميم بطاقة تفاصيل الراتب */
.salary-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;
}
.salary-header { color: #2563eb; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 15px; }
.salary-row { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px dashed #f1f5f9; }
.salary-total { font-weight: bold; color: #16a34a; font-size: 1.2em; padding-top: 15px; border-top: 2px solid #e2e8f0; }
.salary-deduct { color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. شريط المدير المالي (رفع ملف الإكسل)
# ==========================================
with st.sidebar:
    st.header("🔒 لوحة تحكم الإدارة")
    password = st.text_input("أدخل كلمة المرور:", type="












