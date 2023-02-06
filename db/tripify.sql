-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 26, 2023 at 04:27 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tripify`
--

-- --------------------------------------------------------

--
-- Table structure for table `aranzman`
--

DROP TABLE IF EXISTS `aranzman`;
CREATE TABLE IF NOT EXISTS `aranzman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) NOT NULL,
  `napomena` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `aranzman_lokacija`
--

DROP TABLE IF EXISTS `aranzman_lokacija`;
CREATE TABLE IF NOT EXISTS `aranzman_lokacija` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_lokacije` int(11) NOT NULL,
  `id_aranzmana` int(11) NOT NULL,
  `slika` blob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_lokacije` (`id_lokacije`),
  KEY `id_aranzmana` (`id_aranzmana`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `aranzman_prevoz`
--

DROP TABLE IF EXISTS `aranzman_prevoz`;
CREATE TABLE IF NOT EXISTS `aranzman_prevoz` (
  `id_prevoza` int(11) NOT NULL,
  `cena` decimal(10,0) NOT NULL,
  `id_aranzmana` int(11) NOT NULL,
  KEY `id_prevoza` (`id_prevoza`),
  KEY `id_aranzmana` (`id_aranzmana`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `aranzman_slike`
--

DROP TABLE IF EXISTS `aranzman_slike`;
CREATE TABLE IF NOT EXISTS `aranzman_slike` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_lokacija` int(32) NOT NULL,
  `id_aranzmana` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_lokacija` (`id_lokacija`),
  KEY `id_aranzmana` (`id_aranzmana`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `drzava`
--

DROP TABLE IF EXISTS `drzava`;
CREATE TABLE IF NOT EXISTS `drzava` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(60) NOT NULL,
  `oznaka` text NOT NULL,
  `id_kontinenta` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_kontinenta` (`id_kontinenta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `kategorija_smestaja`
--

DROP TABLE IF EXISTS `kategorija_smestaja`;
CREATE TABLE IF NOT EXISTS `kategorija_smestaja` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `tip_smestaja` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `kontinent`
--

DROP TABLE IF EXISTS `kontinent`;
CREATE TABLE IF NOT EXISTS `kontinent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `kontinent`
--

INSERT INTO `kontinent` (`id`, `naziv`) VALUES
(1, 'Evropa'),
(2, 'Azija'),
(3, 'Afrika'),
(4, 'Severna Amerika'),
(5, 'Južna Amerika'),
(6, 'Australija sa Okeanijom');

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
CREATE TABLE IF NOT EXISTS `korisnik` (
  `id` int(11) NOT NULL,
  `id_role` int(11) NOT NULL,
  `ime` text NOT NULL,
  `prezime` text NOT NULL,
  KEY `id_role` (`id_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `lokacija`
--

DROP TABLE IF EXISTS `lokacija`;
CREATE TABLE IF NOT EXISTS `lokacija` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` int(11) NOT NULL,
  `oznaka` int(11) NOT NULL,
  `id_drzave` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_drzave` (`id_drzave`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `nacin_placanja`
--

DROP TABLE IF EXISTS `nacin_placanja`;
CREATE TABLE IF NOT EXISTS `nacin_placanja` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tip_placanja` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `opis_smestaja`
--

DROP TABLE IF EXISTS `opis_smestaja`;
CREATE TABLE IF NOT EXISTS `opis_smestaja` (
  `naziv_objekta` text NOT NULL,
  `id_smestaja` int(11) NOT NULL,
  `dodatak_u_sobi` tinyint(1) NOT NULL,
  `id_aranzman` int(11) NOT NULL,
  `id_kategorija_smestaja` int(11) NOT NULL,
  KEY `id_smestaja` (`id_smestaja`),
  KEY `id_aranzman` (`id_aranzman`),
  KEY `id_kategorija_smestaja` (`id_kategorija_smestaja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ponuda`
--

DROP TABLE IF EXISTS `ponuda`;
CREATE TABLE IF NOT EXISTS `ponuda` (
  `id_ponude` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) NOT NULL,
  `id_lokacije` int(32) NOT NULL,
  `lokacija` text NOT NULL,
  `opis_programa` text NOT NULL,
  `slika` blob NOT NULL,
  `pocetak_putovanja` date NOT NULL,
  `kraj_putovanja` date NOT NULL,
  `cena` decimal(10,0) NOT NULL,
  `id_prevoza` int(11) NOT NULL,
  `id_aranzmana` int(11) NOT NULL,
  PRIMARY KEY (`id_ponude`),
  KEY `id_prevoza` (`id_prevoza`),
  KEY `id_aranzmana` (`id_aranzmana`),
  KEY `id_lokacije` (`id_lokacije`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prevoz`
--

DROP TABLE IF EXISTS `prevoz`;
CREATE TABLE IF NOT EXISTS `prevoz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prevoz`
--

INSERT INTO `prevoz` (`id`, `naziv`) VALUES
(1, 'autobus'),
(2, 'avion'),
(3, 'krstarenje'),
(4, 'voz'),
(5, 'samostalni prevoz');

-- --------------------------------------------------------

--
-- Table structure for table `program_putovanja`
--

DROP TABLE IF EXISTS `program_putovanja`;
CREATE TABLE IF NOT EXISTS `program_putovanja` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_ponuda` int(11) NOT NULL,
  `fakultativni_izleti` text NOT NULL,
  `id_aranzmana` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_ponuda` (`id_ponuda`),
  KEY `id_aranzmana` (`id_aranzmana`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `putnik`
--

DROP TABLE IF EXISTS `putnik`;
CREATE TABLE IF NOT EXISTS `putnik` (
  `licna_karta` int(11) NOT NULL AUTO_INCREMENT,
  `ime` text NOT NULL,
  `prezime` text NOT NULL,
  `kontakt_telefon` text NOT NULL,
  `email` text NOT NULL,
  PRIMARY KEY (`licna_karta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `rezervacija`
--

DROP TABLE IF EXISTS `rezervacija`;
CREATE TABLE IF NOT EXISTS `rezervacija` (
  `br_rezervacije` int(11) NOT NULL AUTO_INCREMENT,
  `id_nacin_placanja` int(11) NOT NULL,
  `broj_osoba` int(11) NOT NULL,
  `komentar/napomena` text NOT NULL,
  `status` tinyint(1) NOT NULL,
  `licna_karta` int(11) NOT NULL,
  `id_ponude` int(11) NOT NULL,
  PRIMARY KEY (`br_rezervacije`),
  KEY `id_nacin_placanja` (`id_nacin_placanja`),
  KEY `licna_karta` (`licna_karta`),
  KEY `id_ponude` (`id_ponude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `naziv`) VALUES
(1, 'admin'),
(2, 'korisnik');

-- --------------------------------------------------------

--
-- Table structure for table `slike_smestaja`
--

DROP TABLE IF EXISTS `slike_smestaja`;
CREATE TABLE IF NOT EXISTS `slike_smestaja` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_smestaja` int(11) NOT NULL,
  `id_aranzman-lokacija` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_smestaja` (`id_smestaja`),
  KEY `id_aranzman-lokacija` (`id_aranzman-lokacija`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `smestaj`
--

DROP TABLE IF EXISTS `smestaj`;
CREATE TABLE IF NOT EXISTS `smestaj` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aranzman_lokacija`
--
ALTER TABLE `aranzman_lokacija`
  ADD CONSTRAINT `aranzman_lokacija_ibfk_1` FOREIGN KEY (`id_aranzmana`) REFERENCES `aranzman` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `aranzman_lokacija_ibfk_2` FOREIGN KEY (`id_lokacije`) REFERENCES `lokacija` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `aranzman_prevoz`
--
ALTER TABLE `aranzman_prevoz`
  ADD CONSTRAINT `aranzman_prevoz_ibfk_1` FOREIGN KEY (`id_aranzmana`) REFERENCES `aranzman` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `aranzman_prevoz_ibfk_2` FOREIGN KEY (`id_prevoza`) REFERENCES `prevoz` (`id`);

--
-- Constraints for table `aranzman_slike`
--
ALTER TABLE `aranzman_slike`
  ADD CONSTRAINT `aranzman_slike_ibfk_1` FOREIGN KEY (`id_aranzmana`) REFERENCES `aranzman` (`id`),
  ADD CONSTRAINT `aranzman_slike_ibfk_2` FOREIGN KEY (`id_lokacija`) REFERENCES `lokacija` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `drzava`
--
ALTER TABLE `drzava`
  ADD CONSTRAINT `drzava_ibfk_1` FOREIGN KEY (`id_kontinenta`) REFERENCES `kontinent` (`id`);

--
-- Constraints for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD CONSTRAINT `korisnik_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `lokacija`
--
ALTER TABLE `lokacija`
  ADD CONSTRAINT `lokacija_ibfk_1` FOREIGN KEY (`id_drzave`) REFERENCES `drzava` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `opis_smestaja`
--
ALTER TABLE `opis_smestaja`
  ADD CONSTRAINT `opis_smestaja_ibfk_1` FOREIGN KEY (`id_aranzman`) REFERENCES `aranzman` (`id`),
  ADD CONSTRAINT `opis_smestaja_ibfk_2` FOREIGN KEY (`id_smestaja`) REFERENCES `smestaj` (`id`),
  ADD CONSTRAINT `opis_smestaja_ibfk_3` FOREIGN KEY (`id_kategorija_smestaja`) REFERENCES `kategorija_smestaja` (`id`);

--
-- Constraints for table `ponuda`
--
ALTER TABLE `ponuda`
  ADD CONSTRAINT `ponuda_ibfk_1` FOREIGN KEY (`id_prevoza`) REFERENCES `prevoz` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ponuda_ibfk_2` FOREIGN KEY (`id_aranzmana`) REFERENCES `aranzman` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ponuda_ibfk_3` FOREIGN KEY (`id_lokacije`) REFERENCES `lokacija` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `program_putovanja`
--
ALTER TABLE `program_putovanja`
  ADD CONSTRAINT `program_putovanja_ibfk_1` FOREIGN KEY (`id_ponuda`) REFERENCES `ponuda` (`id_ponude`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `program_putovanja_ibfk_2` FOREIGN KEY (`id_aranzmana`) REFERENCES `aranzman` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `rezervacija`
--
ALTER TABLE `rezervacija`
  ADD CONSTRAINT `rezervacija_ibfk_1` FOREIGN KEY (`id_nacin_placanja`) REFERENCES `nacin_placanja` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `rezervacija_ibfk_2` FOREIGN KEY (`licna_karta`) REFERENCES `putnik` (`licna_karta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `rezervacija_ibfk_3` FOREIGN KEY (`id_ponude`) REFERENCES `ponuda` (`id_ponude`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `slike_smestaja`
--
ALTER TABLE `slike_smestaja`
  ADD CONSTRAINT `slike_smestaja_ibfk_1` FOREIGN KEY (`id_smestaja`) REFERENCES `smestaj` (`id`),
  ADD CONSTRAINT `slike_smestaja_ibfk_2` FOREIGN KEY (`id_aranzman-lokacija`) REFERENCES `aranzman_lokacija` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
