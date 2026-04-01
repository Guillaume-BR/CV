import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", page_icon="💼", layout="wide")

# CSS personnalisé
st.markdown(
    """
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
    
    /* Tableau des projets */
    .projets-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 20px;
    }
    
    .projets-table td {
        vertical-align: top;
        background-color: #252538;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #2d2d44;
        width: 33.33%;
    }
    
    .projets-table td:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: transform 0.3s;
    }
    
    .projet-titre {
        color: #ffffff;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .projet-date {
        color: #667BC6;
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .projet-description {
        color: #e0e0e0;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    
    .projet-technos {
        color: #e0e0e0;
        margin-bottom: 15px;
    }
    
    .projet-technos-title {
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .projet-lien {
        display: inline-block;
        color: #667BC6;
        text-decoration: none;
        font-weight: 600;
    }
    
    .projet-lien:hover {
        color: #7d8fd9;
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
""",
    unsafe_allow_html=True,
)

# Sidebar


def get_image_base64(image_path):
    """Convertit une image en base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None


with st.sidebar:
    # Convertir l'image en base64
    img_base64 = get_image_base64("data/identite.jpeg")

    if img_base64:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_base64}"
                     style="width: 150px;
                            height: 150px;
                            border-radius: 50%;
                            object-fit: cover;
                            border: 3px solid #667BC6;
                            margin: 20px auto;
                            display: block;"
                     alt="Photo de profil">
                <h3 style='color: #667BC6; margin-top: 10px;'>Guillaume Bernard-Reymond</h3>
                <p style='color: #b0b0b0; font-size: 14px;'>Data Scientist - Python/R - MLOps</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Image non trouvée dans data/identite.jpeg")

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
            "titre": "Projet 1 - Duo-SQL",
            "description": "Création d'une application d'entraînement aux requêtes SQL selon le principe de la répétition espacée avec une base de données de questions",
            "technos": ["Python", "Streamlit", "SQL", "DuckDB"],
            "lien": "https://duo-sql.streamlit.app",
            "image": "data/duo-sql.png",
            "date": "Mars 2026",
        },
        {
            "titre": "Projet 2 - Segmentation d'une séquence ADN",
            "description": "Création d'une application de segmentation d'une séquence ADN en utilisant des algorithmes basés sur les châines de Markov cachées.",
            "technos": ["R", "HMM", "Shiny"],
            "lien": "https://guillaumebr.shinyapps.io/segmention",
            "image": "data/segmentation.png",
            "date": "Février 2026",
        },
        {
            "titre": "Projet 3 - La durée d'hospitalisation",
            "description": "Création d'une application de prévision de la durée d'hospitalisation en fonction de différents paramètres.",
            "technos": ["Python", "ScikitLearn", "Xgboost", "Streamlit", "FastAPI"],
            "lien": "https://duree-hospitalisation.streamlit.app/",
            "image": "data/hospitalisation.png",
            "date": "Novembre 2025",
        },
        {
            "titre": "Projet 4 - Le fléau des féminicides",
            "description": "Création d'une application de visualisation des données sur les féminicides en France.",
            "technos": ["Python", "Streamlit", "OpenAI", "Geopy", "Geopandas"],
            "lien": "https://femicide-france.streamlit.app/",
            "image": "data/feminicide.png",
            "date": "Septembre 2025",
        },
        {
            "titre": "Projet 5 - Picross",
            "description": "Développement d'un jeu de Picross en Shiny",
            "technos": ["R", "Shiny"],
            "lien": "https://maxencelamure.shinyapps.io/Picross",
            "image": "data/picross.png",
            "date": "Mars 2024",
        },
        {
            "titre": "Projet 6 - Occitanie Quality Air Explorer",
            "description": "Projet de groupe sur la visualisation du taux de polluants dans l'air de certaines villes d'Occitanie",
            "technos": [
                "Python",
                "Shiny-Python",
                "API",
                "Quarto",
                "GitHub Pages",
                "CI/CD",
            ],
            "lien": "https://gagginilorenzo.github.io/HAX712X_group5_project/q.html",
            "image": "data/oqae.png",
            "date": "Novembre 2023",
        },
        {
            "titre": "Projet 7 - Meteo Montpeul",
            "description": "Prévision météorologique à Montpellier sur 4 jours",
            "technos": ["Python", "API météo", "Quarto", "GitHub Pages", "CI/CD"],
            "lien": "https://guillaume-br.github.io/meteo-gbr/",
            "image": "data/meteo.png",
            "date": "Octobre 2023",
        },
    ]

    n_cols = 3
    n_rows = (len(projets) + n_cols - 1) // n_cols  # Nombre de lignes nécessaires

    for row in range(n_rows):
        # Ligne des titres
        cols_titre = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_titre[col_idx]:
                    st.markdown(f"### {projets[projet_idx]['titre']}")

        # Ligne des dates
        cols_date = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_date[col_idx]:
                    st.markdown(
                        f"<p style='color: #667BC6; font-size: 14px;'>📅 {projets[projet_idx]['date']}</p>",
                        unsafe_allow_html=True,
                    )

        # Ligne des images
        cols_image = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_image[col_idx]:
                    projet = projets[projet_idx]
                    try:
                        img = Image.open(projet["image"])
                        buffered = BytesIO()
                        img.save(buffered, format="PNG")
                        img_str = base64.b64encode(buffered.getvalue()).decode()

                        st.markdown(
                            f"""
                            <a href="{projet["lien"]}" target="_blank" style="text-decoration: none;">
                                <img src="data:image/png;base64,{img_str}" 
                                     style="width: 100%; 
                                            height: 200px; 
                                            object-fit: cover; 
                                            border-radius: 8px; 
                                            cursor: pointer;
                                            transition: transform 0.2s, box-shadow 0.2s;" 
                                     onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 4px 15px rgba(102, 123, 198, 0.5)';"
                                     onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none';"
                                     alt="{projet["titre"]}">
                            </a>
                        """,
                            unsafe_allow_html=True,
                        )
                    except Exception as e:
                        st.error(f"Image non trouvée: {projet['image']}")

        # Ligne des descriptions
        cols_desc = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_desc[col_idx]:
                    st.markdown(
                        f"""
                        <div style='min-height: 60px; color: #e0e0e0; margin: 10px 0;'>
                            {projets[projet_idx]["description"]}
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

        # Ligne des technologies
        cols_tech = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_tech[col_idx]:
                    st.markdown("**Technologies :**")
                    technos_html = "<div style='min-height: 100px;'>"
                    for techno in projets[projet_idx]["technos"]:
                        technos_html += (
                            f"<p style='color: #e0e0e0; margin: 5px 0;'>• {techno}</p>"
                        )
                    technos_html += "</div>"
                    st.markdown(technos_html, unsafe_allow_html=True)

        # Ligne des liens
        cols_lien = st.columns(n_cols)
        for col_idx in range(n_cols):
            projet_idx = row * n_cols + col_idx
            if projet_idx < len(projets):
                with cols_lien[col_idx]:
                    st.markdown(f"[🔗 Voir le projet]({projets[projet_idx]['lien']})")

        # Séparateur entre les lignes de projets
        if row < n_rows - 1:
            st.markdown("---")


# Page CV
elif page == "📄 CV":
    st.title("📄 Curriculum Vitae")
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        #    # Photo de profil (utiliser la même que la sidebar)
        #    img_base64 = get_image_base64("data/identite.jpeg")
        #    if img_base64:
        #        st.markdown(f"""
        #            <div style="text-align: center;">
        #                <img src="data:image/jpeg;base64,{img_base64}"
        #                     style="width: 200px;
        #                            height: 200px;
        #                            border-radius: 50%;
        #                            object-fit: cover;
        #                            border: 3px solid #667BC6;
        #                            margin: 20px auto;
        #                            display: block;"
        #                     alt="Photo de profil">
        #            </div>
        #        """, unsafe_allow_html=True)

        st.markdown("### 📋 Informations")
        st.write("📧 guillaume.bernardreymond@gmail.com")
        st.write("📱 +33 6 12 63 31 42")
        st.write("📍 Montpellier, France")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/guillaume-bernardreymond)")
        st.write("💻 [GitHub](https://github.com/Guillaume-BR/)")

        st.markdown("### 🌐 Langues")
        st.write("🇫🇷 Français - Langue maternelle")
        st.write("🇬🇧 Anglais - Professionnel")

        try:
            with open("data/cv.pdf", "rb") as pdf_file:
                pdf_bytes = pdf_file.read()

                # Encoder le PDF en base64 pour le téléchargement
                pdf_base64 = base64.b64encode(pdf_bytes).decode()

                st.markdown(
                    f"""
                    <a href="data:application/pdf;base64,{pdf_base64}" 
                       download="CV_Guillaume_Bernard-Reymond.pdf"
                       style="text-decoration: none;">
                        <div style="
                            background: #252538;
                            color: white;
                            padding: 15px 30px;
                            border-radius: 50px;
                            text-align: center;
                            font-weight: bold;
                            font-size: 16px;
                            border: 3px solid #667BC6;
                            cursor: pointer;
                            transition: all 0.3s ease;
                            display: inline-block;
                            box-shadow: 0 4px 15px rgba(102, 123, 198, 0.3);"
                            onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(102, 123, 198, 0.5)';"
                            onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(102, 123, 198, 0.3)';">
                            ⬇️ Télécharger le CV en PDF
                        </div>
                    </a>
                """,
                    unsafe_allow_html=True,
                )

        except FileNotFoundError:
            # Fallback vers GitHub si le fichier n'est pas trouvé localement
            st.markdown(
                """
                <a href="https://raw.githubusercontent.com/Guillaume-BR/CV/main/data/cv.pdf" 
                   download="CV_Guillaume_Bernard-Reymond.pdf"
                   target="_blank"
                   style="text-decoration: none;">
                    <div style="
                        background: linear-gradient(135deg, #667BC6 0%, #8B9FE8 100%);
                        color: white;
                        padding: 15px 30px;
                        border-radius: 50px;
                        text-align: center;
                        font-weight: bold;
                        font-size: 16px;
                        border: 3px solid #667BC6;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        display: inline-block;
                        box-shadow: 0 4px 15px rgba(102, 123, 198, 0.3);"
                        onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(102, 123, 198, 0.5)';"
                        onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(102, 123, 198, 0.3)';">
                        ⬇️ Télécharger le CV en PDF
                    </div>
                </a>
            """,
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown("## 👨‍💼 Expérience Professionnelle")

        st.markdown("### **Stagiaire en Data Science et Modélisation** | Engie-Green")
        st.write("*Mars 2025 - Août 2025*")
        st.write(
            "**Création de jumeaux numériques de parcs éoliens par Machine Learning :**"
        )
        st.write(
            "• Extraction, fiabilisation et analyse de bases de données issues de capteurs"
        )
        st.write("• Implémentation et comparaison de modèles de Machine Learning")
        st.write("• Analyse de résultats physiques et extraction d'insights")
        st.write("• Rédaction de rapport de synthèse")
        st.write(
            "• Communication et présentation de résultats à une équipe pluridisciplinaire"
        )

        st.markdown("### **Enseignant de Mathématiques** | Éducation Nationale")
        st.write("*2009 - 2024*")
        st.write("• Enseignement en collège, lycée et CPGE")
        st.write(
            "• Responsable d'équipe d'enseignants pour la coordination entre pairs"
        )
        st.write("• Formateur de professeurs stagiaires")
        st.write(
            "• Concepteur/Correcteur de sujets de concours (Olympiades, CRPE, CCP)"
        )

        st.markdown("---")

        st.markdown("## 🛠️ Compétences")

        col_skill1, col_skill2, col_skill3 = st.columns(3)

        with col_skill1:
            st.markdown("**💻 Informatique**")
            st.write("• Python / R")
            st.write("• SQL")
            st.write("• Bash / Linux")
            st.write("• Git / GitHub")
            st.write("• Streamlit / Shiny")
            st.write("• Machine Learning / Deep Learning")
            st.write("• Tests unitaires")

        with col_skill2:
            st.markdown("**📊 Data Science**")
            st.write("• Data visualisation")
            st.write("• Dashboards interactifs")
            st.write("• Pipelines ML/DL")
            st.write("• Bases de données SQL")
            st.write("• Analyse statistique")
            st.write("• Modélisation statistique")
            st.write("• Tests statistiques")

        with col_skill3:
            st.markdown("**🤝 Compétences transversales**")
            st.write("• Travail en équipe")
            st.write("• Leadership")
            st.write("• Gestion de projet")
            st.write("• Résolution de conflits")
            st.write("• Communication")
            st.write("• Planification")
            st.write("• Office / Office365")

        st.markdown("---")

        st.markdown("## 🎓 Formations")

        st.markdown(
            "### **Master en Statistiques et Sciences des Données** | Université de Montpellier"
        )
        st.write("*Septembre 2023 - Août 2025 | Mention Très Bien*")
        st.write(
            "Modélisation statistique et probabiliste • Tests statistiques • Machine Learning • Gestion de bases de données • Développement de packages • Production de dashboards"
        )

        st.markdown(
            "### **Agrégation Externe de Mathématiques** | Université de Grenoble"
        )
        st.write("*Septembre 2007 - Août 2008 | Reçu au rang 180*")

        st.markdown(
            "### **Master en Mathématiques Fondamentales** | Université de Grenoble"
        )
        st.write("*Septembre 2006 - Août 2009 | Mention Assez Bien*")
        st.write("Théorie géométrique des groupes • Géométrie Riemannienne")


# Page Contact
elif page == "📧 Contact":
    st.title("📧 Me Contacter")
    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("## 📬 Informations de Contact")
        st.write("📧 guillaume.bernardreymond@gmail.com")
        st.write("📱 +33 6 12 63 31 42")
        st.write("📍 Montpellier, France")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/guillaume-bernardreymond)")
        st.write("💻 [GitHub](https://github.com/Guillaume-BR/)")

    # with col2:
    #    st.markdown("## ✉️ Envoyez-moi un message")
    #
    #    # Formulaire Formspree
    #    st.markdown("""
    #    <form action="https://formspree.io/f/VOTRE_FORM_ID" method="POST" style="display: flex; flex-direction: column; gap: 15px;">
    #        <div>
    #            <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Nom</label>
    #            <input type="text" name="name" required
    #                   style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
    #        </div>
    #
    #        <div>
    #            <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Email</label>
    #            <input type="email" name="email" required
    #                   style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
    #        </div>
    #
    #        <div>
    #            <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Sujet</label>
    #            <input type="text" name="subject" required
    #                   style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px;">
    #        </div>
    #
    #        <div>
    #            <label style="color: #e0e0e0; display: block; margin-bottom: 5px;">Message</label>
    #            <textarea name="message" rows="6" required
    #                      style="width: 100%; padding: 10px; background-color: #2d2d44; color: #e0e0e0; border: 1px solid #667BC6; border-radius: 5px; resize: vertical;"></textarea>
    #        </div>
    #
    #        <button type="submit"
    #                style="background-color: #667BC6; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: 600;">
    #            Envoyer 📤
    #        </button>
    #    </form>
    #    """, unsafe_allow_html=True)
    #
    #    st.markdown("""
    #    <div style='margin-top: 20px; padding: 15px; background-color: #2d2d44; border-radius: 5px; border-left: 4px solid #667BC6;'>
    #        <p style='margin: 0; color: #b0b0b0; font-size: 14px;'>
    #            💡 <strong>Pour activer ce formulaire :</strong><br>
    #            1. Créez un compte gratuit sur <a href='https://formspree.io' target='_blank' style='color: #667BC6;'>formspree.io</a><br>
    #            2. Créez un nouveau formulaire<br>
    #            3. Remplacez "VOTRE_FORM_ID" dans le code par votre ID Formspree
    #        </p>
    #    </div>
    #    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>© 2024 - Guillaume Bernard-Reymond | Créé avec ❤️ et Streamlit</p>
    </div>
""",
    unsafe_allow_html=True,
)
