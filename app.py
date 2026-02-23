import streamlit as st
import pandas as pd

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="نظام الرواتب", page_icon="💰", layout="wide") # جعلنا العرض wide ليناسب الجدول

# ==========================================
# 2. إخفاء حقوق المنصة
# ==========================================
st.markdown("""
<style>
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. العناوين الرئيسية
# ==========================================
st.markdown("<h1 style='text-align: center; direction: rtl;'>نظام الرواتب الإلكتروني</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569; direction: rtl;'>جامعة ابن سينا للعلوم الطبية والصيدلانية</h3>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 4. لوحة الإدارة (صندوق منسدل)
# ==========================================
with st.expander("🔒 لوحة الإدارة (اضغط هنا لرفع ملف الإكسل)"):
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# ==========================================
# 5. واجهة الموظفين (البحث وعرض الجدول)
# ==========================================
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
emp_name = st.text_input("📝 يرجى إدخال اسمك الرباعي أو اللقب للبحث:")
st.markdown("</div>", unsafe_allow_html=True)

# أضفنا تنسيق للزر ليكون بالمنتصف
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
                # تصميم الجدول الأفقي
                # ==========================================
                st.markdown(f"""
                <div style="direction: rtl; overflow-x: auto; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
                    <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: 'Arial', sans-serif; min-width: 1000px;">
                        <thead>
                            <tr>
                                <th colspan="3" style="border: 1px solid #cbd5e1; padding: 12px; background-color: #f8fafc; color: #334155;">البيانات الأساسية</th>
                                <th colspan="5" style="border: 1px solid #cbd5e1; padding: 12px; background-color: #e0f2fe; color: #0369a1;">الاستحقاقات (د.ع)</th>
                                <th colspan="2" style="border: 1px solid #cbd5e1; padding: 12px; background-color: #fee2e2; color: #b91c1c;">الاستقطاعات (د.ع)</th>
                                <th rowspan="2" style="border: 1px solid #cbd5e1; padding: 12px; background-color: #dcfce7; color: #15803d; font-size: 1.1em; vertical-align: middle;">الراتب الصافي</th>
                            </tr>
                            <tr>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f1f5f9;">الاسم</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f1f5f9;">المنصب</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f1f5f9;">اللقب العلمي</th>
                                
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f0f9ff;">الراتب الاسمي</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f0f9ff;">الخدمة الجامعية</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f0f9ff;">النقل</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #f0f9ff;">الزوجية</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #bae6fd; font-weight: bold;">الراتب الكامل</th>
                                
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #fef2f2;">التقاعد</th>
                                <th style="border: 1px solid #cbd5e1; padding: 10px; background-color: #fef2f2;">الضريبة</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap; font-weight: bold;">{row['الاسم']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['المنصب']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['اللقب العلمي']}</td>
                                
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['الراتب الاسمي']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['الخدمة الجامعية']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['النقل']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap;">{row['الزوجية']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap; font-weight: bold; background-color: #e0f2fe;">{row['الراتب الكامل']}</td>
                                
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap; color: #dc2626;">{row['التقاعد']}</td>
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap; color: #dc2626;">{row['الضريبة']}</td>
                                
                                <td style="border: 1px solid #cbd5e1; padding: 15px; white-space: nowrap; font-weight: bold; color: #16a34a; background-color: #f0fdf4; font-size: 1.2em;">{row['الراتب الصافي بعد الاستقطاعات']}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
                st.error("❌ عذراً، لم يتم العثور على اسم مطابق. يرجى التأكد من كتابة الاسم بشكل صحيح.")
                st.markdown("</div>", unsafe_allow_html=True)
                
        except FileNotFoundError:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error("⚠️ لم يتم رفع ملف الرواتب من قبل الإدارة بعد. يرجى من المدير رفع الملف من القائمة أعلاه.")
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
            st.error(f"⚠️ يوجد خطأ في قراءة بيانات الإكسل، تأكد من مطابقة أسماء الأعمدة. (التفاصيل: {e})")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
        st.warning("⚠️ الرجاء إدخال الاسم أولاً.")
        st.markdown("</div>", unsafe_allow_html=True)
