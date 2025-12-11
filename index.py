import streamlit as st
from PIL import Image
import base64

# Configuration de la page
st.set_page_config(
    page_title="Mon Portfolio",
    page_icon="💼",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #1e1e2e;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #252538;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #252538;
    }
    
    /* Header styling */
    header[data-testid="stHeader"] {
        background-color: #252538;
    }
    
    /* Radio buttons in sidebar */
    [data-testid="stSidebar"] .stRadio > label {
        color: #e0e0e0;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #e0e0e0;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #667BC6;
    }
    
    .projet-card {
        border: 2px solid #2d2d44;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        transition: transform 0.3s;
        background-color: #252538;
    }
    .projet-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .contact-info {
        font-size: 18px;
        line-height: 2;
        color: #e0e0e0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    
    p, div, span, li {
        color: #e0e0e0;
    }
    
    .profile-circle {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #667BC6;
        box-shadow: 0 4px 15px rgba(102, 123, 198, 0.3);
        margin: 0 auto;
        display: block;
    }
    
    .stMarkdown a {
        color: #667BC6;
    }

    /* Images des projets - hauteur fixe */
    .projet-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    
    /* Input fields styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #2d2d44;
        color: #e0e0e0;
        border: 1px solid #667BC6;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #667BC6;
        color: white;
    }
    
    .stButton > button:hover {
        background-color: #7d8fd9;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    #st.image("data/identite.jpeg")
    #st.markdown("<h3 style='text-align: center; color: #667BC6;'>Guillaume Bernard-Reymond</h3>", unsafe_allow_html=True)
    #Photo de profil en cercle dans la sidebar
    st.markdown("""
        <img src="data/identite.jpeg" 
             class="profile-circle" 
             style="width: 150px; height: 150px; margin: 20px auto;" 
             alt="Photo de profil">
        <h3 style='text-align: center; color: #667BC6;'>Guillaume Bernard-Reymond</h3>
        <p style='text-align: center; color: #b0b0b0; font-size: 14px;'>Data Scientist - Python/R - MLOps</p>
    """, unsafe_allow_html=True)
    
    st.title("Navigation 🧭")
    page = st.radio("", ["🏠 Projets", "📄 CV", "📧 Contact"])
    
    st.markdown("---")
    st.markdown("### À propos")
    st.write("Portfolio interactif créé avec Streamlit")
    

# Page Projets
if page == "🏠 Projets":
    st.title("🚀 Mes Projets")
    st.markdown("---")
    
    # Exemple de projets (à personnaliser)
    projets = [
        
        {
            "titre": "Projet 1 - La durée d'hospitalisation",
            "description": "Création d'une application de prévision de la durée d'hospitalisation en fonction de différents paramètres.",
            "technos": ["Python", "ScikitLearn" , "Xgboost",  "Streamlit","FastAPI" ],
            "lien": "https://duree-hospitalisation.streamlit.app/",
            "image": "data/hospitalisation.png",
            "date": "Novembre 2025"
        },
        {
            "titre": "Projet 2 - Le fléau des féminicides",
            "description": "Création d'une",
            "technos": ["Python", "Streamlit", "OpenAI", "Geopy","Geopandas"],
            "lien": "https://femicide-france.streamlit.app/",
            "image": "data/feminicide.png",
            "date": "Septembre 2025"
        },
        {
            "titre": "Projet 3 - Picross",
            "description": "Développement d'un jeu de Picross en Shiny",
            "technos": ["R", "Shiny"],
            "lien": "maxencelamure.shinyapps.io/Picross",
            "image": "data/picross.png",
            "date": "Mars 2024"
        },
        {
            "titre": "Projet 4 - Occitanie Quality Air Explorer",
            "description": "Projet de groupe sur la visualisation du taux de polluants dans l'air de certaines villes d'Occitanie",
            "technos": ["Python", "Shiny-Python","Quarto", "GitHub Pages", "CI/CD"],
            "lien": "https://gagginilorenzo.github.io/HAX712X_group5_project/q.html",
            "image": "data/oqae.png",
            "date": "Novembre 2023"
        },
        {
            "titre": "Projet 5 - Meteo Montpeul",
            "description": "Prévision météorologique à Montpellier sur 4 jours",
            "technos": ["Python", "API météo" , "Quarto" , "GitHub Pages", "CI/CD"],
            "lien": "https://guillaume-br.github.io/meteo-gbr/",
            "image": "data/meteo.png",
            "date": "Octobre 2023"
        },

    ]
    

       # Affichage des projets en grille
    cols = st.columns(3)
    for idx, projet in enumerate(projets):
        with cols[idx % 3]:
            # Titre avec date
            st.markdown(f"### {projet['titre']}")
            st.markdown(f"<p style='color: #667BC6; font-size: 14px; margin-top: -10px;'>📅 {projet['date']}</p>", 
                       unsafe_allow_html=True)
            
            # Image avec hauteur fixe via HTML
            st.markdown(f"""
                <img src="{projet['image']}" class="projet-image" alt="{projet['titre']}">
            """, unsafe_allow_html=True)
            st.write(projet['description'])
            
            # Affichage des technos en bullet points
            st.markdown("**Technologies :**")
            for techno in projet['technos']:
                st.markdown(f"• {techno}")
            
            st.markdown(f"[🔗 Voir le projet]({projet['lien']})")
            st.markdown("---") 

    # Affichage des projets en grille
    cols = st.columns(3)
    for idx, projet in enumerate(projets):
        with cols[idx % 3]:
            st.markdown(f"### {projet['titre']}")
            st.image(projet['image'], use_container_width=True)
            st.write(projet['description'])
            
            # Affichage des technos en bullet points
            st.markdown("**Technologies :**")
            for techno in projet['technos']:
                st.markdown(f"• {techno}")
            
            st.markdown(f"[🔗 Voir le projet]({projet['lien']})")
            st.markdown("---")


# Page CV
elif page == "📄 CV":
    st.title("📄 Curriculum Vitae")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/200x200/667BC6/ffffff?text=Photo", width=200)
        st.markdown("### Informations")
        st.write("📧 guillaume.bernardreymond@gmail.com")
        st.write("📱 +33 6 12 63 31 42")
        st.write("📍 Montpellier, France")
        st.write("🔗 [LinkedIn](www.linkedin.com/in/guillaume-bernardreymond)")
        st.write("💻 [GitHub](https://github.com/Guillaume-BR/)")
    
    with col2:
        st.markdown("## 👨‍💻 Expérience Professionnelle")
        
        st.markdown("### **Poste Actuel** | Entreprise")
        st.write("*Janvier 2023 - Présent*")
        st.write("- Description de vos responsabilités")
        st.write("- Réalisations principales")
        st.write("- Technologies utilisées")
        
        st.markdown("### **Poste Précédent** | Entreprise")
        st.write("*Mars 2021 - Décembre 2022*")
        st.write("- Description de vos responsabilités")
        st.write("- Réalisations principales")
        
        st.markdown("---")
        st.markdown("## 🎓 Formation")
        
        st.markdown("### **Diplôme** | École/Université")
        st.write("*2018 - 2021*")
        st.write("Spécialisation en informatique")
        
        st.markdown("---")
        st.markdown("## 🛠️ Compétences")
        
        col_skill1, col_skill2, col_skills3 = st.columns(3)
        
        with col_skills1:
            st.markdown("**Compétences**")
            st.write("• Data visualiation / dashboards")
            st.write("• Pipeline Machine Learning / Deep Learning")
            st.write("• Shiny")
            st.write("• Streamlit")

        with col_skill2:
            st.markdown("**Langages**")
            st.write("• Bash/Linux")
            st.write("• Python")
            st.write("• SQL")
            st.write("• R")
            
        with col_skill3:
            st.markdown("**Frameworks**")
            st.write("• Streamlit")
            st.write("• Shiny")
            st.write("• Streamlit")

        

# Page Contact
elif page == "📧 Contact":
    st.title("📧 Me Contacter")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## 📬 Informations de Contact")
        st.markdown("""
        <div class='contact-info'>
            📧 <strong>Email:</strong> votre.email@exemple.com<br>
            📱 <strong>Téléphone:</strong> +33 6 12 34 56 78<br>
            📍 <strong>Localisation:</strong> Paris, France<br>
            💼 <strong>LinkedIn:</strong> <a href='#'>linkedin.com/in/votreprofil</a><br>
            💻 <strong>GitHub:</strong> <a href='#'>github.com/votre-username</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("## ✉️ Envoyez-moi un message")
        
        # Formulaire Formspree
        st.markdown("""
        <form action="https://formspree.io/f/VOTRE_FORM_ID" method="POST" style="display: flex; flex-direction: column; gap: 15px;">
            <div>
                <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Nom</label>
                <input type="text" name="name" required 
                       style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
            </div>
            
            <div>
                <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Email</label>
                <input type="email" name="email" required 
                       style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
            </div>
            
            <div>
                <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Sujet</label>
                <input type="text" name="subject" required 
                       style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
            </div>
            
            <div>
                <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Message</label>
                <textarea name="message" rows="6" required 
                          style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px; resize: vertical;"></textarea>
            </div>
            
            <button type="submit" 
                    style="background-color: #667BC6; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: 600;">
                Envoyer 📤
            </button>
        </form>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='margin-top: 20px; padding: 15px; background-color: #2d2d44; border-radius: 5px; border-left: 4px solid #667BC6;'>
            <p style='margin: 0; color: #b0b0b0; font-size: 14px;'>
                💡 <strong>Pour activer ce formulaire :</strong><br>
                1. Créez un compte gratuit sur <a href='https://formspree.io' target='_blank' style='color: #667BC6;'>formspree.io</a><br>
                2. Créez un nouveau formulaire<br>
                3. Remplacez "VOTRE_FORM_ID" dans le code par votre ID Formspree
            </p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>© 2024 - Guillaume Bernard-Reymond | Créé avec ❤️ et Streamlit</p>
    </div>
""", unsafe_allow_html=True)