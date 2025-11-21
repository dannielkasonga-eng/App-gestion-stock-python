-- script de réinitialisation de la base de données gestion_stock --
-- Connectez-vous à mysql en entrant vos informations de connexion utilisateur --

USE gestion_stock;

-- Désactivation temporaire de vérification des clés étrangères --

SET FOREIGN_KEYS_CHECKS = 0;

-- suppression de toutes les tables --

DROP TABLE IF EXISTS fournisseurs;
DROP TABLE IF EXISTS employes;
DROP TABLE IF EXISTS produits;
DROP TABLE IF EXISTS gestion_entree;
DROP TABLE IF EXISTS ligne_entree;
DROP TABLE IF EXISTS gestion_sortie;
DROP TABLE IF EXISTS ligne_sortie;

-- réactivation des clés étrangères --

SET FOREIGN_KEY_CHEKS = 1;

-- recréation des tables --

-- table des fournisseurs

CREATE TABLE IF NOT EXISTS fournisseurs (
    id_fournisseurs INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    matricule VARCHAR(12) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    adresse VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    statut TINYINT(1) UNSIGNED DEFAULT 1 COMMENT '1=actif, 0=inactif'
) ENGINE = INNODB;

-- table des employes

CREATE TABLE employes (
    id_employes INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    matricule VARCHAR(10) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    genre ENUM('M', 'F') NOT NULL,
    adresse VARCHAR(100) NOT NULL, 
    mobile VARCHAR(15) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    fonction ENUM('Pharmacien adjoint', 'assistant', 'caissier', 'magasinier', 'comptable') NOT NULL,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut TINYINT(1) UNSIGNED DEFAULT 1 COMMENT '1=actif, 0=inactif'
) ENGINE = INNODB;

-- table des produits

CREATE TABLE IF NOT EXISTS produits (
    id_produits BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_fournisseur BIGINT UNSIGNED NOT NULL, 
    ref_produit VARCHAR(13) NOT NULL, 
    code_atc VARCHAR(7) NOT NULL,
    nom_commercial VARCHAR(50) NOT NULL,
    dci VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    forme VARCHAR(50) NOT NULL,
    conditionnement VARCHAR(100) NOT NULL,
    stock_minimum INT UNSIGNED NOT NULL DEFAULT 0, 
    stock_maximum INT UNSIGNED NOT NULL DEFAULT 0, 
    description_produit TEXT NULL,
    statut TINYINT(1) UNSIGNED DEFAULT 1 COMMENT '1=actif, 0=inactif', 
    
    CONSTRAINT fk_produit_fournisseur 
        FOREIGN KEY (id_fournisseur) 
        REFERENCES fournisseurs (id_fournisseurs)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- table gestion_entree

CREATE TABLE gestion_entree (
    id_entrees BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_fournisseur BIGINT UNSIGNED NOT NULL, 
    date_commande TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut_commande ENUM('en cours', 'validee', 'annulee') DEFAULT 'en cours',
    date_reception TIMESTAMP NULL,
    observation TEXT NULL,
    
    CONSTRAINT fk_entree_fournisseur 
        FOREIGN KEY(id_fournisseur) 
        REFERENCES fournisseurs(id_fournisseurs)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- table ligne_entree

CREATE TABLE ligne_entree (
    id_ligne BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_entree BIGINT UNSIGNED NOT NULL, 
    id_produit BIGINT UNSIGNED NOT NULL, 
    numero_lot VARCHAR(30) NOT NULL,
    peremption DATE NOT NULL,
    quantite INT UNSIGNED NOT NULL,
    prix_unitaire_entree DECIMAL(10, 2) NOT NULL, 
    emplacement ENUM('Z-PMO', 'Z-TAC', 'Z-ER', 'Z-Q',) NULL, 

    CONSTRAINT fk_ligne_entree_entetes 
        FOREIGN KEY(id_entree) 
        REFERENCES gestion_entree(id_entrees)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_ligne_entree_produit
        FOREIGN KEY(id_produit) 
        REFERENCES produits(id_produits)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB ;

-- table gestion_sortie

CREATE TABLE gestion_sortie (
    id_sorties BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_employe INT UNSIGNED NOT NULL, 
    date_sortie TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    destinataire ENUM('particulier', 'professionnel') NOT NULL,
    statut ENUM('libre d''accès', 'sous ordonnance') NULL,
    observation TEXT NULL,
    
    CONSTRAINT fk_sortie_employes
        FOREIGN KEY(id_employe)
        REFERENCES employes(id_employes)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- table ligne_sortie

CREATE TABLE ligne_sortie (
    id_ligne BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_sortie BIGINT UNSIGNED NOT NULL, 
    id_produit BIGINT UNSIGNED NOT NULL, 
    numero_lot VARCHAR(30) NOT NULL,
    peremption DATE NOT NULL,
    quantite INT UNSIGNED NOT NULL,
    prix_unitaire_vente DECIMAL(10, 2) NOT NULL, 
    
    CONSTRAINT fk_ligne_sortie_entetes
        FOREIGN KEY(id_sortie)
        REFERENCES gestion_sortie(id_sorties)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_ligne_sortie_produit 
        FOREIGN KEY(id_produit)
        REFERENCES produits(id_produits)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- recréation des index pour toutes les tables --

-- création index pour la table fournisseurs --

ALTER TABLE fournisseurs 
ADD INDEX idx_id_fournisseurs (id_fournisseurs),
ADD INDEX idx_matricule_nom (matricule, nom);

-- creation index pour la table employes --

ALTER TABLE employes
ADD INDEX idx_id_employes (id_employes),
ADD INDEX idx_matricule_nom_date_creation (matricule, nom, date_creation);

-- création  index pour la table produits --

ALTER TABLE produits
ADD INDEX idx_fk_id_fournisseur_ref_produit(id_fournisseur, ref_produit),
ADD INDEX idx_stock_minimum_maximum(stock_minimum, stock_maximum);

-- création index pour la table gestion_entree --

ALTER TABLE gestion_entree
ADD INDEX idx_fk_id_fournisseur(id_fournisseur),
ADD INDEX idx_statut_commande_date_commande(statut_commande, date_commande),
ADD INDEX idx_date_reception(date_reception);

-- création index pour la table ligne_entree --

ALTER TABLE ligne_entree
ADD INDEX idx_fk_id_entree_produit(id_entree, id_produit),
ADD INDEX idx_numero_lot_peremption(numero_lot, peremption);

-- création index pour la table gestion_sortie --

ALTER TABLE gestion_sortie
ADD INDEX idx_id_employe_date_sortie(id_employe, id_sortie);


-- création  index ligne_sortie --

ALTER TABLE ligne_sortie
ADD INDEX idx_fk_sortie_produit(id_sortie, id_produit),
ADD INDEX idx_numero_lot_peremption(numero_lot, peremption);


SELECT 'Base de données gestion_commande réinitialisée avec succès !' as message;
SELECT 'Toutes les tables ont été supprimées et recréées vides sans index.' as info;