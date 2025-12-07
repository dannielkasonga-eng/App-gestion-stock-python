-- script pour la création de la base de données gestion_stock --
-- mysql -u root -p < create_database.sql --

-- Création de la base de données --
CREATE DATABASE IF NOT EXISTS gestion_stock 
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE gestion_stock;

-- Création de la table fournisseurs --
CREATE TABLE IF NOT EXISTS fournisseurs (
    id_fournisseurs BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    matricule CHAR(14) NOT NULL UNIQUE,
    nom VARCHAR(50) NOT NULL,
    adresse VARCHAR(100) NOT NULL,
    mobile VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    statut TINYINT(1) UNSIGNED DEFAULT 1 COMMENT '1=actif, 0=inactif'
) ENGINE = INNODB;

-- Création de la table employes --
CREATE TABLE employes (
    id_employes BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    matricule CHAR(10) NOT NULL UNIQUE,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    genre ENUM('M', 'F') NOT NULL,
    adresse VARCHAR(100) NOT NULL, 
    mobile VARCHAR(20) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    fonction ENUM('Pharmacien adjoint', 'Assistant', 'Caissier', 'Magasinier', 'Comptable') DEFAULT 'Assistant',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut TINYINT(1) UNSIGNED DEFAULT 1 COMMENT '1=actif, 0=inactif'
) ENGINE = INNODB;

-- Création de la table produits --
CREATE TABLE IF NOT EXISTS produits (
    id_produits BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_fournisseurs BIGINT UNSIGNED NOT NULL, 
    ref_produit VARCHAR(6) NOT NULL UNIQUE, 
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
        FOREIGN KEY (id_fournisseurs) 
        REFERENCES fournisseurs (id_fournisseurs)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- Création de la table gestion_entree --
CREATE TABLE gestion_entree (
    id_entrees BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_fournisseurs BIGINT UNSIGNED NOT NULL, 
    date_commande TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut_commande ENUM('En cours', 'Validee', 'Annulee') DEFAULT 'En cours',
    date_reception TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    observation TEXT NULL,
    
    CONSTRAINT fk_entree_fournisseur 
        FOREIGN KEY(id_fournisseurs) 
        REFERENCES fournisseurs(id_fournisseurs)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- Création de la table ligne_entree --
CREATE TABLE ligne_entree (
    id_ligne BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_entrees BIGINT UNSIGNED NOT NULL, 
    id_produits BIGINT UNSIGNED NOT NULL, 
    numero_lot VARCHAR(30) NOT NULL,
    peremption DATE NOT NULL,
    quantite INT UNSIGNED NOT NULL,
    prix_unitaire_entree DECIMAL(10, 2) NOT NULL, 
    emplacement ENUM('Z-PMO', 'Z-TAC', 'Z-ER', 'Z-Q') NULL, 

    CONSTRAINT fk_ligne_entree_entetes 
        FOREIGN KEY(id_entrees) 
        REFERENCES gestion_entree(id_entrees)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_ligne_entree_produit
        FOREIGN KEY(id_produits) 
        REFERENCES produits(id_produits)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB ;

-- Création de la table gestion_sortie --

CREATE TABLE gestion_sortie (
    id_sorties BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_employes BIGINT UNSIGNED NOT NULL, 
    date_sortie TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    destinataire ENUM ('Particulier', 'Professionnel')  DEFAULT 'Particulier',
    statut ENUM('Vente libre', 'Sous ordonnance') NULL,
    observation TEXT NULL,
    
    CONSTRAINT fk_sortie_employes
        FOREIGN KEY(id_employes)
        REFERENCES employes(id_employes)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- Création de la table ligne_sortie --
CREATE TABLE ligne_sortie (
    id_ligne BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_sorties BIGINT UNSIGNED NOT NULL, 
    id_produits BIGINT UNSIGNED NOT NULL, 
    numero_lot VARCHAR(30) NOT NULL,
    peremption DATE NOT NULL,
    quantite INT UNSIGNED NOT NULL,
    prix_unitaire_vente DECIMAL(10, 2) NOT NULL, 
    
    CONSTRAINT fk_ligne_sortie_entetes
        FOREIGN KEY(id_sorties)
        REFERENCES gestion_sortie(id_sorties)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_ligne_sortie_produit 
        FOREIGN KEY(id_produits)
        REFERENCES produits(id_produits)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
) ENGINE = INNODB;

-- insertions des données fictives pour toutes les tables --

-- Remplissage de la table fournisseurs
INSERT INTO fournisseurs (matricule, nom, adresse, mobile, email, statut) VALUES
('NEWC243LIME001', 'NEW CESAMEX', 'Av. Kasa-Vubu, Lingwala, Kinshasa', '+243 970 111 001', 'contact@newcesamex.cd', 1),
('ZENL243LIME002', 'ZENUPHA LABORATOIRES', 'Av. Libération, Limete, Kinshasa', '+243 970 111 002', 'info@zenupha.cd', 1),
('CAIP243LIME003', 'CAISA PHARMA INTERNATIONAL', 'Bd Lumumba, Limete, Kinshasa', '+243 970 111 003', 'contact@caisa.cd', 1),
('PRIP243LIME004', 'PRINCE PHARMA SARL', 'Av. du Commerce, Limete, Kinshasa', '+243 970 111 004', 'contact@princepharma.cd', 1),
('UNIP243LIME005', 'UNIQUE PHARMA SARL', 'Av. Kikwit n°45, Limete, Kinshasa', '+243 970 111 005', 'contact@uniquepharma.cd', 1),
('PROS243GOME006', 'PROMED S.A.R.L.', 'Av. de la Justice, Gombe, Kinshasa', '+243 970 111 006', 'info@promedlabo.cd', 1);

-- remplissage de la table employes
INSERT INTO employes (matricule, nom, prenom, date_naissance, genre, adresse, mobile, email, fonction, statut) VALUES
('EMPKAJE001', 'KABONGO', 'Jean', '1985-03-12', 'M', 'Av. de la Justice, Gombe, Kinshasa', '+243970111001', 'jean.kabongo@example.com', 'Pharmacien adjoint', 1),
('EMPMALI002', 'MUKENDI', 'Alice', '1990-07-23', 'F', 'Av. Lumumba, Limete, Kinshasa', '+243970111002', 'alice.mukendi@example.com', 'Assistant', 1),
('EMPPATP003', 'NGOMA', 'Patrick', '1982-11-05', 'M', 'Av. Kasa-Vubu, Ngaliema, Kinshasa', '+243970111003', 'patrick.ngoma@example.com', 'Caissier', 1),
('EMPTMAR004', 'TUMBA', 'Marie', '1993-01-18', 'F', 'Av. Kabinda, Bandalungwa, Kinshasa', '+243970111004', 'marie.tumba@example.com', 'Magasinier', 1),
('EMPLPAU005', 'LOKONI', 'Paul', '1987-09-30', 'M', 'Av. du Port, Gombe, Kinshasa', '+243970111005', 'paul.lokoni@example.com', 'Comptable', 1),
('EMPSOPP006', 'BASENGE', 'Sophie', '1991-06-12', 'F', 'Av. Kikwit, Limete, Kinshasa', '+243970111006', 'sophie.basenge@example.com', 'Assistant', 1),
('EMPEMMP007', 'MBUYI', 'Emmanuel', '1984-12-21', 'M', 'Av. de la Révolution, Masina, Kinshasa', '+243970111007', 'emmanuel.mbuyi@example.com', 'Pharmacien adjoint', 1),
('EMPKCHR008', 'KABILA', 'Christine', '1995-08-14', 'F', 'Av. de la Victoire, Ngaliema, Kinshasa', '+243970111008', 'christine.kabila@example.com', 'Caissier', 1),
('EMPNMIC009', 'NDONGALA', 'Michel', '1988-02-25', 'M', 'Av. du Commerce, Limete, Kinshasa', '+243970111009', 'michel.ndongala@example.com', 'Magasinier', 1),
('EMPMCAT010', 'MBULU', 'Catherine', '1992-05-10', 'F', 'Av. des Huileries, Matete, Kinshasa', '+243970111010', 'catherine.mbulu@example.com', 'Comptable', 1);


-- remplissage de la table produits 
INSERT INTO produits (id_fournisseurs, ref_produit, code_atc, nom_commercial, dci, dosage, forme, conditionnement, stock_minimum, stock_maximum, description_produit, statut) VALUES
(1,'REF001','A010AA1','Doliprane','Paracétamol','500mg','Comprimé','Boîte de 10 comprimés pelliculés',50,500,'Analgésique et antipyrétique',1),
(1,'REF002','A020AA2','Panadol','Paracétamol','650mg','Comprimé','Boîte de 12 comprimés effervescents',50,400,'Soulage la douleur',1),
(2,'REF003','B010AB1','Amoxil','Amoxicilline','500mg','Capsule','Boîte de 14 capsules molles',30,300,'Antibiotique à large spectre',1),
(2,'REF004','B020AC2','Augmentin','Amoxicilline/Acide clavulanique','875mg/125mg','Comprimé','Boîte de 12 comprimés filmés',30,250,'Antibiotique combiné',1),
(3,'REF005','C010AD1','Ibuprofène','Ibuprofène','400mg','Comprimé','Boîte de 20 comprimés à libération prolongée',40,350,'Anti-inflammatoire',1),
(3,'REF006','C020AE1','Nurofen','Ibuprofène','200mg','Comprimé','Boîte de 16 comprimés filmés',40,300,'Antidouleur',1),
(4,'REF007','D010AF1','Ciproflox','Ciprofloxacine','500mg','Comprimé','Boîte de 10 comprimés pelliculés',20,200,'Antibiotique fluoroquinolone',1),
(4,'REF008','D020AG1','Ciproxin','Ciprofloxacine','250mg','Comprimé','Boîte de 12 comprimés filmés',20,180,'Traitement infections bactériennes',1),
(5,'REF009','E010AH1','Ventolin','Salbutamol','100mcg','Inhalateur','Inhalateur doseur 200 sprays',10,150,'Bronchodilatateur',1),
(5,'REF010','E020AI1','Asmanex','Mometasone','220mcg','Inhalateur','Inhalateur doseur 120 sprays',10,120,'Corticostéroïde inhalé',1),
(6,'REF011','F010AJ1','Lansoprazole','Lansoprazole','30mg','Capsule','Boîte de 14 capsules gastro-résistantes',25,200,'Inhibiteur de la pompe à protons',1),
(5,'REF012','F020AK1','Oméprazole','Oméprazole','20mg','Capsule','Boîte de 14 capsules gastro-résistantes',25,220,'Antiacide',1),
(4,'REF013','G010AL1','Lipitor','Atorvastatine','20mg','Comprimé','Boîte de 30 comprimés pelliculés',15,150,'Réducteur de cholestérol',1),
(4,'REF014','G020AM1','Crestor','Rosuvastatine','10mg','Comprimé','Boîte de 28 comprimés pelliculés',15,140,'Statine',1),
(4,'REF015','H010AN1','Metformine','Metformine','500mg','Comprimé','Boîte de 30 comprimés à libération prolongée',40,400,'Antidiabétique oral',1),
(4,'REF016','H020AO1','Glucophage','Metformine','850mg','Comprimé','Boîte de 30 comprimés pelliculés',40,380,'Gère le diabète type 2',1),
(4,'REF017','I010AP1','Aspirine','Acide acétylsalicylique','100mg','Comprimé','Boîte de 20 comprimés effervescents',30,300,'Anti-inflammatoire et anticoagulant',1),
(4,'REF018','I020AQ1','Aspegic','Acide acétylsalicylique','500mg','Comprimé','Boîte de 20 comprimés pelliculés',30,250,'Soulage douleur et inflammation',1),
(5,'REF019','J010AR1','Paracétamol 650','Paracétamol','650mg','Comprimé','Boîte de 12 comprimés effervescents',50,400,'Antalgique et antipyrétique',1),
(3,'REF020','J020AS1','Ibuprofène 400','Ibuprofène','400mg','Comprimé','Boîte de 16 comprimés filmés',40,350,'Anti-inflammatoire',1),
(2,'REF021','A030AT1','Amoxiclav','Amoxicilline/Acide clavulanique','500mg/125mg','Comprimé','Boîte de 12 comprimés filmés',30,250,'Antibiotique combiné',1),
(2,'REF022','B030AU1','Azithromycine','Azithromycine','500mg','Comprimé','Boîte de 6 comprimés pelliculés',20,200,'Antibiotique à large spectre',1),
(3,'REF023','C030AV1','Diclofénac','Diclofénac','50mg','Comprimé','Boîte de 20 comprimés à libération prolongée',35,300,'Anti-inflammatoire',1),
(4,'REF024','D030AW1','Naproxène','Naproxène','250mg','Comprimé','Boîte de 14 comprimés pelliculés',35,280,'Anti-inflammatoire',1),
(5,'REF025','E030AX1','Salbutamol','Salbutamol','100mcg','Inhalateur','Inhalateur doseur 150 sprays',10,150,'Bronchodilatateur',1),
(6,'REF026','F030AY1','Ranitidine','Ranitidine','150mg','Comprimé','Boîte de 20 comprimés gastro-résistants',25,220,'Antiacide',1),
(4,'REF027','G030AZ1','Simvastatine','Simvastatine','20mg','Comprimé','Boîte de 30 comprimés pelliculés',15,150,'Réducteur de cholestérol',1),
(4,'REF028','H030BA1','Gliclazide','Gliclazide','80mg','Comprimé','Boîte de 30 comprimés à libération prolongée',40,380,'Antidiabétique',1),
(4,'REF029','I030BB1','Diclofénac','Diclofénac','100mg','Comprimé','Boîte de 20 comprimés filmés',35,300,'Anti-inflammatoire',1),
(5,'REF030','J030BC1','Oméprazole','Oméprazole','20mg','Capsule','Boîte de 14 capsules gastro-résistantes',25,220,'Anti-acide gastrique',1);

-- remplissage de la table gestion_entree

-- Gestion des entrées par fournisseur
INSERT INTO gestion_entree (id_fournisseurs, date_commande, statut_commande, date_reception, observation) VALUES
(1, NOW() - INTERVAL 10 DAY, 'Validee', NOW() - INTERVAL 8 DAY, 'Stock initial'),
(2, NOW() - INTERVAL 9 DAY, 'Validee', NOW() - INTERVAL 7 DAY, 'Stock initial'),
(3, NOW() - INTERVAL 8 DAY, 'Validee', NOW() - INTERVAL 6 DAY, 'Stock initial'),
(4, NOW() - INTERVAL 7 DAY, 'Validee', NOW() - INTERVAL 5 DAY, 'Stock initial'),
(5, NOW() - INTERVAL 6 DAY, 'Validee', NOW() - INTERVAL 4 DAY, 'Stock initial'),
(6, NOW() - INTERVAL 5 DAY, 'Validee', NOW() - INTERVAL 3 DAY, 'Stock initial'),
(4, NOW() - INTERVAL 4 DAY, 'Validee', NOW() - INTERVAL 2 DAY, 'Stock initial'),
(4, NOW() - INTERVAL 3 DAY, 'Validee', NOW() - INTERVAL 1 DAY, 'Stock initial'),
(3, NOW() - INTERVAL 2 DAY, 'Validee', NOW(), 'Stock initial'),
(6, NOW() - INTERVAL 1 DAY, 'Validee', NOW(), 'Stock initial');


-- remplissage de la table ligne_entree

-- Ligne d'entrée par produit (30 produits répartis sur 10 entrées)
INSERT INTO ligne_entree (id_entrees, id_produits, numero_lot, peremption, quantite, prix_unitaire_entree, emplacement) VALUES
(1, 1, 'LOT1001', NOW() + INTERVAL 730 DAY, 200, 500, 'Z-PMO'),
(1, 2, 'LOT1002', NOW() + INTERVAL 730 DAY, 180, 650, 'Z-PMO'),
(2, 3, 'LOT2001', NOW() + INTERVAL 1095 DAY, 150, 1200, 'Z-TAC'),
(2, 4, 'LOT2002', NOW() + INTERVAL 1095 DAY, 140, 2000, 'Z-TAC'),
(3, 5, 'LOT3001', NOW() + INTERVAL 365 DAY, 250, 800, 'Z-ER'),
(3, 6, 'LOT3002', NOW() + INTERVAL 365 DAY, 220, 900, 'Z-ER'),
(4, 7, 'LOT4001', NOW() + INTERVAL 730 DAY, 120, 1500, 'Z-Q'),
(4, 8, 'LOT4002', NOW() + INTERVAL 730 DAY, 100, 1800, 'Z-Q'),
(5, 9, 'LOT5001', NOW() + INTERVAL 730 DAY, 130, 2500, 'Z-PMO'),
(5, 10, 'LOT5002', NOW() + INTERVAL 730 DAY, 110, 3000, 'Z-PMO'),
(6, 11, 'LOT6001', NOW() + INTERVAL 365 DAY, 140, 1800, 'Z-TAC'),
(6, 12, 'LOT6002', NOW() + INTERVAL 365 DAY, 150, 1700, 'Z-TAC'),
(7, 13, 'LOT7001', NOW() + INTERVAL 1095 DAY, 100, 3500, 'Z-ER'),
(7, 14, 'LOT7002', NOW() + INTERVAL 1095 DAY, 90, 4000, 'Z-ER'),
(8, 15, 'LOT8001', NOW() + INTERVAL 730 DAY, 200, 800, 'Z-Q'),
(8, 16, 'LOT8002', NOW() + INTERVAL 730 DAY, 190, 900, 'Z-Q'),
(9, 17, 'LOT9001', NOW() + INTERVAL 365 DAY, 160, 400, 'Z-PMO'),
(9, 18, 'LOT9002', NOW() + INTERVAL 365 DAY, 150, 500, 'Z-PMO'),
(10, 19, 'LOT10001', NOW() + INTERVAL 730 DAY, 180, 450, 'Z-TAC'),
(10, 20, 'LOT10002', NOW() + INTERVAL 730 DAY, 170, 600, 'Z-TAC'),
(1, 21, 'LOT10003', NOW() + INTERVAL 1095 DAY, 140, 2000, 'Z-ER'),
(2, 22, 'LOT20003', NOW() + INTERVAL 1095 DAY, 130, 2500, 'Z-ER'),
(3, 23, 'LOT30003', NOW() + INTERVAL 365 DAY, 160, 900, 'Z-Q'),
(4, 24, 'LOT40003', NOW() + INTERVAL 365 DAY, 150, 1000, 'Z-Q'),
(5, 25, 'LOT50003', NOW() + INTERVAL 730 DAY, 120, 2500, 'Z-PMO'),
(6, 26, 'LOT60003', NOW() + INTERVAL 730 DAY, 110, 2700, 'Z-PMO'),
(7, 27, 'LOT70003', NOW() + INTERVAL 1095 DAY, 100, 1500, 'Z-TAC'),
(8, 28, 'LOT80003', NOW() + INTERVAL 1095 DAY, 90, 1700, 'Z-TAC'),
(9, 29, 'LOT90003', NOW() + INTERVAL 365 DAY, 200, 800, 'Z-ER'),
(10, 30, 'LOT100003', NOW() + INTERVAL 365 DAY, 190, 900, 'Z-ER');


-- Sorties enregistrées par les employés
INSERT INTO gestion_sortie (id_employes, date_sortie, destinataire, statut, observation) VALUES
(1, NOW() - INTERVAL 9 DAY, 'Particulier', 'Vente libre', 'Vente comptoir Doliprane'),
(2, NOW() - INTERVAL 8 DAY, 'Particulier', 'Sous ordonnance', 'Vente sur ordonnance'),
(3, NOW() - INTERVAL 7 DAY, 'Professionnel', 'Vente libre', 'Approvisionnement clinique locale'),
(4, NOW() - INTERVAL 6 DAY, 'Particulier', 'Vente libre', 'Demande client directe'),
(5, NOW() - INTERVAL 5 DAY, 'Professionnel', 'Sous ordonnance', 'Distribution à pharmacie partenaire'),
(6, NOW() - INTERVAL 4 DAY, 'Particulier', 'Vente libre', 'Vente de routine'),
(7, NOW() - INTERVAL 3 DAY, 'Particulier', 'Sous ordonnance', 'Ordonnance patient chronique'),
(8, NOW() - INTERVAL 2 DAY, 'Professionnel', 'Vente libre', 'Sortie vers dépôt médical'),
(9, NOW() - INTERVAL 1 DAY, 'Particulier', 'Sous ordonnance', 'Traitement court terme'),
(10,NOW() - INTERVAL 10 DAY, 'Professionnel', 'Vente libre', 'Vente à établissement partenaire');


-- remplissage de la table ligne_sortie

-- Lignes de sortie (quantités raisonnables et produits variés)
INSERT INTO ligne_sortie (id_sorties, id_produits, numero_lot, peremption, quantite, prix_unitaire_vente) VALUES
(1, 1, 'LOT1001', NOW() + INTERVAL 730 DAY, 20, 650),
(1, 2, 'LOT1002', NOW() + INTERVAL 730 DAY, 15, 800),
(2, 3, 'LOT2001', NOW() + INTERVAL 1095 DAY, 10, 1500),
(2, 4, 'LOT2002', NOW() + INTERVAL 1095 DAY, 8, 2600),
(3, 5, 'LOT3001', NOW() + INTERVAL 365 DAY, 25, 950),
(3, 6, 'LOT3002', NOW() + INTERVAL 365 DAY, 18, 1100),
(4, 7, 'LOT4001', NOW() + INTERVAL 730 DAY, 12, 1800),
(4, 8, 'LOT4002', NOW() + INTERVAL 730 DAY, 10, 2200),
(5, 9, 'LOT5001', NOW() + INTERVAL 730 DAY, 15, 3100),
(5, 10, 'LOT5002', NOW() + INTERVAL 730 DAY, 14, 3500),
(6, 11, 'LOT6001', NOW() + INTERVAL 365 DAY, 20, 2100),
(6, 12, 'LOT6002', NOW() + INTERVAL 365 DAY, 18, 2000),
(7, 13, 'LOT7001', NOW() + INTERVAL 1095 DAY, 9, 4200),
(7, 14, 'LOT7002', NOW() + INTERVAL 1095 DAY, 10, 4800),
(8, 15, 'LOT8001', NOW() + INTERVAL 730 DAY, 22, 950),
(8, 16, 'LOT8002', NOW() + INTERVAL 730 DAY, 18, 1100),
(9, 17, 'LOT9001', NOW() + INTERVAL 365 DAY, 16, 500),
(9, 18, 'LOT9002', NOW() + INTERVAL 365 DAY, 15, 650),
(10, 19, 'LOT10001', NOW() + INTERVAL 730 DAY, 20, 600),
(10, 20, 'LOT10002', NOW() + INTERVAL 730 DAY, 18, 750),
(1, 21, 'LOT10003', NOW() + INTERVAL 1095 DAY, 10, 2500),
(2, 22, 'LOT20003', NOW() + INTERVAL 1095 DAY, 8, 3100),
(3, 23, 'LOT30003', NOW() + INTERVAL 365 DAY, 12, 1100),
(4, 24, 'LOT40003', NOW() + INTERVAL 365 DAY, 14, 1250),
(5, 25, 'LOT50003', NOW() + INTERVAL 730 DAY, 9, 3100),
(6, 26, 'LOT60003', NOW() + INTERVAL 730 DAY, 10, 3300),
(7, 27, 'LOT70003', NOW() + INTERVAL 1095 DAY, 8, 1900),
(8, 28, 'LOT80003', NOW() + INTERVAL 1095 DAY, 7, 2100),
(9, 29, 'LOT90003', NOW() + INTERVAL 365 DAY, 15, 950),
(10, 30, 'LOT100003', NOW() + INTERVAL 365 DAY, 14, 1100);


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
ADD INDEX idx_fk_id_fournisseurs_ref_produit(id_fournisseurs, ref_produit),
ADD INDEX idx_stock_minimum_maximum(stock_minimum, stock_maximum);

-- création index pour la table gestion_entree --

ALTER TABLE gestion_entree
ADD INDEX idx_fk_id_fournisseurs(id_fournisseurs),
ADD INDEX idx_statut_commande_date_commande(statut_commande, date_commande),
ADD INDEX idx_date_reception(date_reception);

-- création index pour la table ligne_entree --

ALTER TABLE ligne_entree
ADD INDEX idx_fk_id_entree_produit(id_entrees, id_produits),
ADD INDEX idx_numero_lot_peremption(numero_lot, peremption);

-- création index pour la table gestion_sortie --

ALTER TABLE gestion_sortie
ADD INDEX idx_fk_id_employes(id_employes),
ADD INDEX idx_date_sortie(date_sortie);


-- création  index ligne_sortie --

ALTER TABLE ligne_sortie
ADD INDEX idx_fk_sorties_produits(id_sorties, id_produits),
ADD INDEX idx_numero_lot_peremption(numero_lot, peremption);

-- affichage des informations de création --
SELECT 'Base de données gestion_stock créee avec succès !' as message;
SELECT 'Nombre de lignes total contenu dans chaque table :' as info;
SELECT COUNT(*) as nb_fournisseurs FROM fournisseurs;
SELECT COUNT(*) as nb_employes FROM employes;
SELECT COUNT(*) as nb_produits FROM produits;
SELECT COUNT(*) as nb_gestion_entree FROM gestion_entree;
SELECT COUNT(*) as nb_ligne_entree FROM ligne_entree;
SELECT COUNT(*) as nb_gestion_sortie FROM gestion_sortie;
SELECT COUNT(*) as nb_ligne_sortie FROM ligne_sortie;

SELECT
  (SELECT COUNT(*) FROM fournisseurs) +
  (SELECT COUNT(*) FROM employes) +
  (SELECT COUNT(*) FROM produits) +
  (SELECT COUNT(*) FROM gestion_entree) +
  (SELECT COUNT(*) FROM ligne_entree) +
  (SELECT COUNT(*) FROM gestion_sortie) +
  (SELECT COUNT(*) FROM ligne_sortie)
  AS total_lignes;


