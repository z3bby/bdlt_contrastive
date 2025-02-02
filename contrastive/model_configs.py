import json

# Note on the configurations: Not all optimizers need all parameters.
# They are included for easier usage in main.py
CONFIG_PATH = "./models/model_configs.json"
CONFIGS = {"Pairwise_SGD": {"learning_manager": {"train_mode": "pairwise", "model_name": "Pairwise_SGD",
                                                 "encoder": None},
                            "training": {"epochs": 10, "batch_size": 16, "optimizer_name": "sgd", "lr": 0.0055,
                                         "momentum": 0.7, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                         "trust_coef": 0.001}},

           "Pairwise_RMS": {"learning_manager": {"train_mode": "pairwise", "model_name": "Pairwise_RMS",
                                                 "encoder": None},
                            "training": {"epochs": 10, "batch_size": 16, "optimizer_name": "rmsprop", "lr": 0.00005,
                                         "momentum": 0, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                         "trust_coef": 0.001}},

           "Pairwise_LARS": {"learning_manager": {"train_mode": "pairwise", "model_name": "Pairwise_LARS",
                                                  "encoder": None},
                             "training": {"epochs": 10, "batch_size": 16, "optimizer_name": "lars", "lr": 0.0075,
                                          "momentum": 0.15, "weight_decay": 0, "alpha": 0.99, "eps": 6e-09,
                                          "trust_coef": 0.005}},


           "Triplet_SGD": {"learning_manager": {"train_mode": "triplet", "model_name": "Triplet_SGD",
                                                "encoder": None},
                           "training": {"epochs": 10, "batch_size": 8, "optimizer_name": "sgd", "lr": 0.0015,
                                        "momentum": 0.75, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                        "trust_coef": 0.001}},

           "Triplet_RMS": {"learning_manager": {"train_mode": "triplet", "model_name": "Triplet_RMS",
                                                "encoder": None},
                           "training": {"epochs": 10, "batch_size": 8, "optimizer_name": "rmsprop", "lr": 0.00005,
                                        "momentum": 0, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                        "trust_coef": 0.001}},

           "Triplet_LARS": {"learning_manager": {"train_mode": "triplet", "model_name": "Triplet_LARS",
                                                 "encoder": None},
                            "training": {"epochs": 10, "batch_size": 8, "optimizer_name": "lars", "lr": 0.03,
                                         "momentum": 0.85, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                         "trust_coef": 0.001}},



           "InfoNCE_SGD": {"learning_manager": {"train_mode": "infoNCE", "model_name": "InfoNCE_SGD",
                                                "encoder": None},
                           "training": {"epochs": 10, "batch_size": 4, "optimizer_name": "sgd", "lr": 0.003,
                                        "momentum": 0.55, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                        "trust_coef": 0.001}},

           "InfoNCE_RMS": {"learning_manager": {"train_mode": "infoNCE", "model_name": "InfoNCE_RMS",
                                                "encoder": None},
                           "training": {"epochs": 10, "batch_size": 4, "optimizer_name": "rmsprop", "lr": 0.00005,
                                        "momentum": 0, "weight_decay": 0, "alpha": 0.99, "eps": 1e-08,
                                        "trust_coef": 0.001}},

           "InfoNCE_LARS": {"learning_manager": {"train_mode": "infoNCE", "model_name": "InfoNCE_LARS",
                                                 "encoder": None},
                            "training": {"epochs": 10, "batch_size": 4, "optimizer_name": "lars", "lr": 0.085,
                                         "momentum": 0, "weight_decay": 0, "alpha": 0.99, "eps": 1.5e-09,
                                         "trust_coef": 0.0005}},
           }


if __name__ == "__main__":
    with open(CONFIG_PATH, 'w') as f:
        json.dump(CONFIGS, f, indent=4)