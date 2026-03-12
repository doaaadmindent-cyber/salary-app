import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="بوابة الرواتب | جامعة ابن سينا", page_icon="🏛️", layout="wide")

# ==========================================
# 2. التصميم الاحترافي (CSS المتقدم)
# ==========================================
st.markdown("""
<style>
    /* إخفاء العلامات الافتراضية لمنصة Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* خلفية النظام العامة */
    .stApp {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* تصميم الشريط الجانبي للإدارة */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 2px solid #0f172a;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p {
        color: #f8fafc !important;
    }

    /* تصميم زر البحث */
    div.stButton > button:first-child {
        background-color: #0369a1;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #0284c7;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    /* تصميم حقل إدخال الاسم */
    div[data-baseweb="input"] {
        border-radius: 8px;
        border: 1px solid #cbd5e1;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
        background-color: white;
    }
    div[data-baseweb="input"] input {
        direction: rtl;
        font-size: 16px;
        padding: 12px;
    }

    /* تصميم بطاقات الملخص العلوية */
    .dashboard-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 4px solid #0369a1;
        text-align: center;
        margin-bottom: 25px;
    }
    .dashboard-title {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .dashboard-value {
        color: #0f172a;
        font-size: 20px;
        font-weight: bold;
    }
    .net-salary-value {
        color: #16a34a;
        font-size: 32px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. شريط الإدارة الجانبي (Sidebar)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; direction: rtl;'>🔒 بوابة الإدارة</h2>", unsafe_allow_html=True)
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    
    password = st.text_input("كلمة مرور المدير:", type="password")
    
    if password == "1234":
        st.success("✅ دخول ناجح")
        uploaded_file = st.file_uploader("📥 رفع كشف الإكسل:", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث الكشوفات!")
    elif password != "":
        st.error("❌ الرمز غير صحيح")
        
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 4. الواجهة الرئيسية (الهيدر الاحترافي)
# ==========================================
st.markdown("""
<div style='background-color: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); text-align: center; margin-bottom: 30px;'>
    <h1 style='color: #0f172a; margin-bottom: 5px; font-size: 36px;'>نظام الاستعلام عن الرواتب</h1>
    <h3 style='color: #64748b; margin-top: 0; font-weight: normal;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. منطقة البحث (موسطة وأنيقة)
# ==========================================
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)

# وضعنا حقل البحث والزر في منتصف الشاشة باستخدام الأعمدة
col_space1, col_search, col_space2 = st.columns([1, 2, 1])

with col_search:
    emp_name = st.text_input("👤 أدخل اسمك الرباعي أو اللقب:", placeholder="اكتب اسمك هنا...")
    search_button = st.button("🔍 استعلام عن الراتب")

st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# ==========================================
# 6. معالجة البيانات وعرض النتائج
# ==========================================
if search_button:
    if emp_name:
        try:
            df = pd.read_excel("salaries.xlsx")
            df['الاسم'] = df['الاسم'].astype(str).str.strip()
            user_data = df[df['الاسم'].str.contains(emp_name.strip(), na=False)]
            
            if not user_data.empty:
                row = user_data.iloc[0]
                
                # --- لوحة البيانات العلوية (Dashboard Cards) ---
                st.markdown("<div style='direction: rtl;'>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                
                with c1:
                    st.markdown(f"""
                    <div class="dashboard-card" style="border-top-color: #16a34a;">
                        <div class="dashboard-title">الراتب الصافي (المستلم)</div>
                        <div class="net-salary-value">{row.get('الراتب الصافي بعد الاستقطاعات', '-')} <span style="font-size: 16px; color: #64748b;">د.ع</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with c2:
                    st.markdown(f"""
                    <div class="dashboard-card">
                        <div class="dashboard-title">المنصب / اللقب العلمي</div>
                        <div class="dashboard-value">{row.get('المنصب', '-')} / {row.get('اللقب العلمي', '-')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with c3:
                    st.markdown(f"""
                    <div class="dashboard-card">
                        <div class="dashboard-title">اسم الموظف</div>
                        <div class="dashboard-value">{row.get('الاسم', '-')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # --- الجدول التفصيلي الأفقي ---
                st.markdown("<h4 style='text-align: right; color: #334155; direction: rtl; margin-top: 20px;'>تفاصيل الاستحقاقات والاستقطاعات:</h4>", unsafe_allow_html=True)
                
                html_table = f"""
                <div style="overflow-x: auto; direction: rtl; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-radius: 8px;">
                  <table style="width: 100%; min-width: 1000px; border-collapse: collapse; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: white;">
                    <thead>
                      <tr style="background-color: #f1f5f9; color: #334155; font-size: 15px;">
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #e0f2fe;">الراتب الاسمي</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #e0f2fe;">الخدمة الجامعية</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #e0f2fe;">النقل</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #e0f2fe;">الزوجية</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #bae6fd;">الراتب الكامل</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #fee2e2;">التقاعد</th>
                        <th style="border: 1px solid #e2e8f0; padding: 15px; background-color: #fee2e2;">الضريبة</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="color: #0f172a; font-size: 16px; font-weight: 500;">
                        <td style="border: 1px solid #e2e8f0; padding: 15px;">{row.get('الراتب الاسمي', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px;">{row.get('الخدمة الجامعية', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px;">{row.get('النقل', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px;">{row.get('الزوجية', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px; font-weight: bold; background-color: #f0f9ff;">{row.get('الراتب الكامل', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px; color: #dc2626;">{row.get('التقاعد', '-')}</td>
                        <td style="border: 1px solid #e2e8f0; padding: 15px; color: #dc2626;">{row.get('الضريبة', '-')}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
                st.markdown(html_table, unsafe_allow_html=True)
                
            else:
                st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
                st.error("❌ عذراً، لم يتم العثور على بيانات بهذا الاسم. يرجى التأكد من الإملاء.")
                st.markdown("</div>", unsafe_allow_html=True)
                
        except FileNotFoundError:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.warning("⚠️ النظام قيد التحديث. لم يتم رفع كشوفات الرواتب لهذا الشهر بعد.")
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error("⚠️ حدث خطأ فني أثناء قراءة البيانات. يرجى مراجعة الإدارة.")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='direction: rtl; text-align: center;'>", unsafe_allow_html=True)
        st.info("👆 يرجى إدخال اسمك في الحقل أعلاه والضغط على زر الاستعلام.")
        st.markdown("</div>", unsafe_allow_html=True)
