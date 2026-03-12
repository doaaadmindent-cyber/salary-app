import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="بوابة الرواتب | جامعة ابن سينا", page_icon="🏛️", layout="wide")

# ==========================================
# 2. التصميم الاحترافي (CSS) وإعدادات ملف الـ PDF
# ==========================================
st.markdown("""
<style>
    /* إخفاء عناصر Streamlit الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* الخلفية العامة للنظام */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* الشريط الجانبي للإدارة */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 1px solid #334155;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p {
        color: #f8fafc !important;
    }

    /* حقل إدخال الرقم الوظيفي داخل الفورم */
    div[data-baseweb="input"] {
        border-radius: 10px;
        border: 2px solid #cbd5e1;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
        background-color: rgba(255, 255, 255, 0.9);
    }
    div[data-baseweb="input"] input {
        direction: rtl;
        font-size: 18px;
        padding: 15px;
        font-weight: bold;
        color: #0f172a;
        text-align: center;
    }

    /* بطاقات المعلومات */
    .info-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
        margin-bottom: 25px;
    }
    .card-icon { font-size: 35px; margin-bottom: 10px; }
    .card-label { color: #64748b; font-size: 15px; margin-bottom: 8px; font-weight: 600; }
    .card-value { color: #1e293b; font-size: 22px; font-weight: 800; }
    .salary-value { color: #059669; font-size: 36px; font-weight: 900; }

    /* ==========================================
       إعدادات ملف الـ PDF (إخفاء الأزرار عند الطباعة)
       ========================================== */
    @media print {
        [data-testid="stSidebar"] { display: none !important; }
        header { display: none !important; }
        [data-testid="stForm"] { display: none !important; }
        iframe { display: none !important; }
        .stApp { background: white !important; }
        .info-card { box-shadow: none !important; border: 2px solid #e2e8f0 !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. شريط الإدارة الجانبي
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; direction: rtl;'>⚙️ لوحة التحكم</h2>", unsafe_allow_html=True)
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    
    password = st.text_input("رمز مرور الإدارة:", type="password")
    
    if password == "1234":
        st.success("✅ تم توثيق الدخول")
        uploaded_file = st.file_uploader("📂 تحديث قاعدة بيانات الرواتب (Excel):", type=["xlsx", "xls"])
        
        if uploaded_file is not None:
            with open("salaries.xlsx", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✨ تم تحديث الرواتب بنجاح!")
    elif password != "":
        st.error("❌ الرمز غير صحيح")
        
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 4. ترويسة النظام
# ==========================================
st.markdown("""
<div style='background: white; padding: 40px 20px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); text-align: center; margin-bottom: 40px; border: 1px solid #e2e8f0;'>
    <div style='font-size: 50px; margin-bottom: 10px;'>🏛️</div>
    <h1 style='color: #0f172a; margin-bottom: 10px; font-size: 38px; font-weight: 800;'>بوابة الرواتب الإلكترونية</h1>
    <h3 style='color: #475569; margin-top: 0; font-weight: 500; font-size: 20px;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. منطقة البحث (استخدام Form لحل مشكلة عدم الاستجابة)
# ==========================================
col_space1, col_search, col_space2 = st.columns([1, 2, 1])

with col_search:
    st.markdown("<div style='direction: rtl; text-align: center; margin-bottom: 15px;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #334155; font-weight: bold;'>يرجى إدخال الرقم الوظيفي الخاص بك للاستعلام:</h4>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # ربط الإدخال والزر في Form واحد
    with st.form(key='search_form'):
        st.markdown("<div style='direction: rtl;'>", unsafe_allow_html=True)
        emp_id = st.text_input("🔑", placeholder="أدخل الرقم الوظيفي هنا...", label_visibility="collapsed")
        # زر مدمج داخل الفورم بتصميم أنيق
        search_button = st.form_submit_button("🔐 عرض كشف الراتب", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# ==========================================
# 6. معالجة البيانات وعرض النتائج
# ==========================================
if search_button:
    if emp_id:
        try:
            df = pd.read_excel("salaries.xlsx")
            df['الرقم الوظيفي'] = df['الرقم الوظيفي'].astype(str).str.strip()
            search_query = str(emp_id).strip()
            
            user_data = df[df['الرقم الوظيفي'] == search_query]
            
            if not user_data.empty:
                row = user_data.iloc[0]
                
                st.markdown("<div style='direction: rtl;'>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                
                with c1:
                    st.markdown(f"""
                    <div class="info-card" style="border-bottom: 4px solid #10b981;">
                        <div class="card-icon">💰</div>
                        <div class="card-label">الصافي للاستلام</div>
                        <div class="salary-value">{row.get('الراتب الصافي بعد الاستقطاعات', '-')} <span style="font-size: 18px; color: #64748b;">د.ع</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with c2:
                    st.markdown(f"""
                    <div class="info-card" style="border-bottom: 4px solid #3b82f6;">
                        <div class="card-icon">💼</div>
                        <div class="card-label">المنصب / اللقب</div>
                        <div class="card-value">{row.get('المنصب', '-')} <br> <span style="font-size: 16px; color: #64748b;">{row.get('اللقب العلمي', '-')}</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with c3:
                    st.markdown(f"""
                    <div class="info-card" style="border-bottom: 4px solid #6366f1;">
                        <div class="card-icon">👤</div>
                        <div class="card-label">معلومات الموظف</div>
                        <div class="card-value">{row.get('الاسم', '-')} <br> <span style="font-size: 14px; color: #64748b; background: #e2e8f0; padding: 2px 8px; border-radius: 10px;">ID: {row.get('الرقم الوظيفي', '-')}</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("<h4 style='text-align: right; color: #1e293b; direction: rtl; margin-top: 30px; font-weight: bold;'>📊 الكشف التفصيلي للمفردات:</h4>", unsafe_allow_html=True)
                
                html_table = f"""
                <div style="overflow-x: auto; direction: rtl; background: white; border-radius: 12px; padding: 1px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); border: 1px solid #e2e8f0;">
                  <table style="width: 100%; min-width: 1000px; border-collapse: collapse; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                    <thead>
                      <tr style="background-color: #f8fafc; color: #475569; font-size: 15px; border-bottom: 2px solid #e2e8f0;">
                        <th style="padding: 18px 15px; font-weight: 600;">الراتب الاسمي</th>
                        <th style="padding: 18px 15px; font-weight: 600;">الخدمة الجامعية</th>
                        <th style="padding: 18px 15px; font-weight: 600;">النقل</th>
                        <th style="padding: 18px 15px; font-weight: 600;">الزوجية</th>
                        <th style="padding: 18px 15px; font-weight: 700; color: #0369a1; background: #f0f9ff;">الراتب الكامل</th>
                        <th style="padding: 18px 15px; font-weight: 600; color: #b91c1c;">التقاعد</th>
                        <th style="padding: 18px 15px; font-weight: 600; color: #b91c1c;">الضريبة</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="color: #0f172a; font-size: 17px; font-weight: 600;">
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9;">{row.get('الراتب الاسمي', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9;">{row.get('الخدمة الجامعية', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9;">{row.get('النقل', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9;">{row.get('الزوجية', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9; background: #f0f9ff; color: #0369a1;">{row.get('الراتب الكامل', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9; color: #ef4444;">{row.get('التقاعد', '-')}</td>
                        <td style="padding: 20px 15px; border-bottom: 1px solid #f1f5f9; color: #ef4444;">{row.get('الضريبة', '-')}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
                st.markdown(html_table, unsafe_allow_html=True)

                # ==========================================
                # زر تحميل ملف الـ PDF عبر الجافاسكربت
                # ==========================================
                st.write("")
                st.write("")
                components.html(
                    """
                    <div style="text-align: center;">
                        <button onclick="window.parent.print()" style="background: linear-gradient(90deg, #10b981 0%, #059669 100%); color: white; border-radius: 10px; border: none; padding: 15px 30px; font-size: 18px; font-weight: bold; cursor: pointer; font-family: Tahoma, Arial; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);">
                            📥 حفظ بصيغة PDF
                        </button>
                    </div>
                    """,
                    height=80
                )
                
            else:
                st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
                st.error("❌ لم يتم العثور على بيانات مطابقة. يرجى التأكد من كتابة الرقم الوظيفي بشكل صحيح.")
                st.markdown("</div>", unsafe_allow_html=True)
                
        except Exception as e:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error("⚠️ حدث خطأ فني أثناء قراءة البيانات. تأكد من رفع كشف الإكسل بشكل صحيح.")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='direction: rtl; text-align: center;'>", unsafe_allow_html=True)
        st.warning("👆 يرجى إدخال الرقم الوظيفي أولاً.")
        st.markdown("</div>", unsafe_allow_html=True)
