import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="wide")

# ==========================================
# 2. إخفاء حقوق المنصة
# ==========================================
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# ==========================================
# 3. شريط الإدارة الجانبي (Sidebar)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; direction: rtl;'>🔒 لوحة الإدارة</h2>", unsafe_allow_html=True)
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    
    password = st.text_input("أدخل كلمة المرور:", type="password")
    
    if password == "1234":
        st.success("✅ تم تسجيل الدخول بنجاح")
        uploaded_file = st.file_uploader("📥 ارفع ملف الإكسل:", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث بيانات الرواتب!")
    elif password != "":
        st.error("❌ كلمة المرور غير صحيحة")
        
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 4. الواجهة الرئيسية (العناوين)
# ==========================================
st.markdown("<h1 style='text-align: center;'>نظام الرواتب الإلكتروني</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 5. واجهة الموظفين (البحث وعرض الجدول الأفقي)
# ==========================================
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
emp_name = st.text_input("📝 يرجى إدخال اسمك الرباعي أو اللقب للبحث:")
st.markdown("</div>", unsafe_allow_html=True)

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
                row = user_data.iloc[0]
                
                # ==========================================
                # كود HTML لجدول أفقي إجباري
                # ==========================================
                html_table = f"""
                <div style="overflow-x: auto; direction: rtl; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 8px;">
                  <table style="width: 100%; min-width: 1200px; border-collapse: collapse; text-align: center; font-family: 'Arial', sans-serif;">
                    <thead>
                      <tr style="background-color: #f8fafc; color: #0f172a; font-size: 16px;">
                        <th style="border: 2px solid #cbd5e1; padding: 12px;">الاسم</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px;">المنصب</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px;">اللقب العلمي</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #e0f2fe; color: #0369a1;">الراتب الاسمي</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #e0f2fe; color: #0369a1;">الخدمة الجامعية</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #e0f2fe; color: #0369a1;">النقل</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #e0f2fe; color: #0369a1;">الزوجية</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #bae6fd; color: #0369a1;">الراتب الكامل</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #fee2e2; color: #b91c1c;">التقاعد</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #fee2e2; color: #b91c1c;">الضريبة</th>
                        <th style="border: 2px solid #cbd5e1; padding: 12px; background-color: #dcfce7; color: #15803d; font-size: 18px;">الراتب الصافي</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="background-color: #ffffff; color: #334155; font-size: 15px; font-weight: bold;">
                        <td style="border: 2px solid #cbd5e1; padding: 12px;">{row.get('الاسم', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px;">{row.get('المنصب', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px;">{row.get('اللقب العلمي', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #f0f9ff;">{row.get('الراتب الاسمي', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #f0f9ff;">{row.get('الخدمة الجامعية', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #f0f9ff;">{row.get('النقل', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #f0f9ff;">{row.get('الزوجية', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #e0f2fe;">{row.get('الراتب الكامل', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #fef2f2; color: #dc2626;">{row.get('التقاعد', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #fef2f2; color: #dc2626;">{row.get('الضريبة', '-')}</td>
                        <td style="border: 2px solid #cbd5e1; padding: 12px; background-color: #f0fdf4; color: #16a34a; font-size: 18px;">{row.get('الراتب الصافي بعد الاستقطاعات', '-')}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
                st.markdown(html_table, unsafe_allow_html=True)
                
            else:
                st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
                st.error("❌ عذراً، لم يتم العثور على اسم مطابق.")
                st.markdown("</div>", unsafe_allow_html=True)
                
        except FileNotFoundError:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error("⚠️ لم يتم رفع ملف الرواتب من قبل الإدارة بعد.")
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error(f"⚠️ يوجد خطأ في قراءة بيانات الإكسل. (التفاصيل: {e})")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
        st.warning("⚠️ الرجاء إدخال الاسم أولاً.")
        st.markdown("</div>", unsafe_allow_html=True)
