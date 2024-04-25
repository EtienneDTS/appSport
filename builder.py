import json

# Ajouter nom de fichier
filename = "./data.json"

def create_dico(filename)-> dict:
    if filename == "":
        print("Veuillez ajouter un nom de fichier")
        return 
    dico = {
        
        "head": {
            "Date": {
                "Start": "2024-04-19",
                "End": "",
            },
            "program": "upper lower 7/7",
            "types": ["U1", "L1", "U2"],
            "Description": "Suivie de la progression de l'entrainement UL concernant les exercices de base",
            "U1": {
                "exercices": {
                    "DC": "Développé couché",
                    "ROWING": "Rowing",
                    "DM": "Développé militaire",
                },
                "builder": {
                    "DC": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "ROWING": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "DM": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    }
                },
                "save": {
                    "DC": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "ROWING": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "DM": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    }
                }
            },
            "L1": {
                "exercices": {
                    "SQT": "Squat",
                    "SDTJT": "Soulevé de terre jambes tendues",
                    "FENTES": "Fentes",
                },
                "builder": {
                    "SQT": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "SDTJT": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "FENTES": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                },
                "save": {
                    "SQT": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "SDTJT": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "FENTES": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    }
                }
            },
            "U2": {
                "exercices": {
                    "DIPS": "Dips lesté",
                    "TRACTIONS": "Tractions lestées",
                    "RM": "Rowing menton",
                },
                "builder": {
                    "DIPS": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "TRACTIONS": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "RM": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    }
                },
                "save": {
                    "DIPS": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "TRACTIONS": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    },
                    "RM": {
                        "Reps": 0,
                        "Weight": 0,
                        "RM": 0,
                    }
                },
            },
            "all_exercices": {
                "DC": "Développé couché", 
                "ROW": "Rowing", 
                "DM": "Développé militaire", 
                "SQT": "Squat",
                "SDTJT": "Soulevé de terre jambes tendues",
                "FENTES": "Fentes",
                "DIPS": "Dips lesté",
                "TRACTIONS": "Tractions lestées",
                "RM": "Rowing menton"
            }
        },
        "data": {}
    }
    with open(filename, "w") as f:
        json.dump(dico, f, indent=4)
        
if __name__ == "__main__":
    create_dico(filename)