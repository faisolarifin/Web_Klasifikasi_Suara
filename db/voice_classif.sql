-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2022 at 03:52 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `voice_classif`
--

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

CREATE TABLE `dataset` (
  `id` int(11) NOT NULL,
  `kelas` varchar(50) NOT NULL,
  `voice_name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dataset`
--

INSERT INTO `dataset` (`id`, `kelas`, `voice_name`) VALUES
(8, 'Abyan', '2022-05-08T14_31_57.392Z.wav'),
(9, 'Abyan', '2022-05-08T14_32_01.000Z.wav'),
(10, 'Abyan', '2022-05-08T14_32_09.599Z.wav'),
(11, 'Abyan', '2022-05-08T14_33_25.809Z.wav'),
(12, 'Abyan', '2022-05-08T14_33_36.329Z.wav'),
(13, 'Abyan', '2022-05-08T14_33_40.200Z.wav'),
(14, 'Abyan', '2022-05-08T14_33_44.577Z.wav'),
(15, 'Abyan', '2022-05-08T14_33_49.576Z.wav'),
(16, 'Abyan', '2022-05-08T14_33_53.717Z.wav'),
(17, 'Abyan', '2022-05-08T14_33_57.977Z.wav'),
(18, 'Abyan', '2022-05-08T14_34_02.143Z.wav'),
(19, 'Abyan', '2022-05-08T14_34_06.551Z.wav'),
(20, 'Abyan', '2022-05-08T14_34_11.143Z.wav'),
(21, 'Abyan', '2022-05-08T14_34_15.300Z.wav'),
(22, 'Abyan', '2022-05-08T14_34_19.574Z.wav'),
(23, 'Abyan', '2022-05-08T14_34_23.595Z.wav'),
(24, 'Abyan', '2022-05-08T14_34_36.348Z.wav'),
(25, 'Abyan', '2022-05-08T14_36_03.879Z.wav'),
(26, 'Abyan', '2022-05-08T14_36_07.439Z.wav'),
(27, 'Abyan', '2022-05-08T14_36_12.281Z.wav'),
(28, 'Abyan', '2022-05-08T14_36_16.079Z.wav'),
(29, 'Abyan', '2022-05-08T14_36_19.897Z.wav'),
(30, 'Abyan', '2022-05-08T14_36_29.232Z.wav'),
(31, 'Abyan', '2022-05-08T14_36_33.380Z.wav'),
(32, 'Abyan', '2022-05-08T14_36_37.091Z.wav'),
(33, 'Abyan', '2022-05-08T14_36_40.839Z.wav'),
(34, 'Abyan', '2022-05-08T14_36_44.898Z.wav'),
(35, 'Abyan', '2022-05-08T14_36_48.554Z.wav'),
(36, 'Abyan', '2022-05-08T14_36_52.337Z.wav'),
(37, 'Abyan', '2022-05-08T14_36_56.064Z.wav'),
(38, 'Abyan', '2022-05-08T14_37_04.953Z.wav'),
(39, 'Abyan', '2022-05-08T14_37_08.652Z.wav'),
(40, 'Abyan', '2022-05-08T14_37_12.370Z.wav'),
(41, 'Abyan', '2022-05-08T14_37_16.212Z.wav'),
(42, 'Abyan', '2022-05-08T14_37_19.998Z.wav'),
(43, 'Abyan', '2022-05-08T14_37_23.851Z.wav'),
(44, 'Abyan', '2022-05-08T14_37_27.624Z.wav'),
(45, 'Abyan', '2022-05-08T14_37_31.801Z.wav'),
(46, 'Abyan', '2022-05-08T14_37_35.716Z.wav'),
(47, 'Abyan', '2022-05-08T14_37_39.817Z.wav'),
(48, 'Abyan', '2022-05-08T14_37_43.762Z.wav'),
(49, 'Abyan', '2022-05-08T14_37_47.790Z.wav'),
(50, 'Abyan', '2022-05-08T14_37_52.042Z.wav'),
(51, 'Ilmi', '2022-05-08T15_05_48.146Z.wav'),
(52, 'Ilmi', '2022-05-08T15_05_51.571Z.wav'),
(53, 'Ilmi', '2022-05-08T15_05_54.991Z.wav'),
(54, 'Ilmi', '2022-05-08T15_05_58.196Z.wav'),
(55, 'Ilmi', '2022-05-08T15_06_01.455Z.wav'),
(56, 'Ilmi', '2022-05-08T15_06_07.449Z.wav'),
(57, 'Ilmi', '2022-05-08T15_06_10.375Z.wav'),
(58, 'Ilmi', '2022-05-08T15_06_18.228Z.wav'),
(59, 'Ilmi', '2022-05-08T15_06_25.911Z.wav'),
(60, 'Ilmi', '2022-05-08T15_07_05.179Z.wav'),
(61, 'Ilmi', '2022-05-08T15_08_20.223Z.wav'),
(62, 'Ilmi', '2022-05-08T15_16_19.357Z.wav'),
(63, 'Ilmi', '2022-05-08T15_16_37.003Z.wav'),
(64, 'Ilmi', '2022-05-08T15_16_40.261Z.wav'),
(65, 'Ilmi', '2022-05-08T15_16_46.528Z.wav'),
(66, 'Ilmi', '2022-05-08T15_16_58.548Z.wav'),
(67, 'Ilmi', '2022-05-08T15_17_04.320Z.wav'),
(68, 'Ilmi', '2022-05-08T15_17_24.146Z.wav'),
(69, 'Ilmi', '2022-05-08T15_17_27.535Z.wav'),
(70, 'Ilmi', '2022-05-08T15_17_30.829Z.wav'),
(71, 'Ilmi', '2022-05-08T15_17_41.038Z.wav'),
(72, 'Ilmi', '2022-05-08T15_25_51.975Z.wav'),
(73, 'Ilmi', '2022-05-08T15_25_57.114Z.wav'),
(74, 'Ilmi', '2022-05-08T15_26_01.125Z.wav'),
(75, 'Ilmi', '2022-05-08T15_26_04.674Z.wav'),
(76, 'Ilmi', '2022-05-08T15_26_07.983Z.wav'),
(77, 'Ilmi', '2022-05-08T15_26_11.364Z.wav'),
(78, 'Ilmi', '2022-05-08T15_26_15.189Z.wav'),
(79, 'Ilmi', '2022-05-08T15_26_18.478Z.wav'),
(80, 'Ilmi', '2022-05-08T15_26_21.876Z.wav'),
(81, 'Ilmi', '2022-05-08T15_26_27.981Z.wav'),
(82, 'Ilmi', '2022-05-08T16_10_18.176Z.wav'),
(83, 'Ilmi', '2022-05-08T16_10_21.636Z.wav'),
(84, 'Ilmi', '2022-05-08T16_10_24.930Z.wav'),
(85, 'Ilmi', '2022-05-08T16_10_28.195Z.wav'),
(86, 'Ilmi', '2022-05-08T16_10_31.491Z.wav'),
(87, 'Ilmi', '2022-05-08T16_10_34.812Z.wav'),
(88, 'Ilmi', '2022-05-08T16_10_38.039Z.wav'),
(89, 'Ilmi', '2022-05-08T16_10_41.044Z.wav'),
(90, 'Ilmi', '2022-05-08T16_10_44.285Z.wav'),
(91, 'Ilmi', '2022-05-08T16_10_47.514Z.wav'),
(92, 'Ilmi', '2022-05-08T16_10_50.755Z.wav'),
(93, 'Ilmi', '2022-05-08T16_10_53.910Z.wav'),
(94, 'Ilmi', '2022-05-08T16_10_57.074Z.wav'),
(95, 'Ilmi', '2022-05-08T16_11_00.288Z.wav'),
(96, 'Ilmi', '2022-05-08T16_11_03.641Z.wav'),
(97, 'Ilmi', '2022-05-08T16_11_06.921Z.wav'),
(98, 'Ilmi', '2022-05-08T16_11_10.096Z.wav'),
(99, 'Ilmi', '2022-05-08T16_11_17.277Z.wav'),
(100, 'Ilmi', '2022-05-08T16_11_20.609Z.wav'),
(101, 'Itsbat', '2022-05-08T14_51_43.224Z.wav'),
(102, 'Itsbat', '2022-05-08T14_51_53.997Z.wav'),
(103, 'Itsbat', '2022-05-08T14_52_04.712Z.wav'),
(104, 'Itsbat', '2022-05-08T14_52_07.921Z.wav'),
(105, 'Itsbat', '2022-05-08T14_52_11.759Z.wav'),
(106, 'Itsbat', '2022-05-08T14_52_19.321Z.wav'),
(107, 'Itsbat', '2022-05-08T14_52_30.711Z.wav'),
(108, 'Itsbat', '2022-05-08T14_52_38.348Z.wav'),
(109, 'Itsbat', '2022-05-08T14_52_42.305Z.wav'),
(110, 'Itsbat', '2022-05-08T14_52_45.366Z.wav'),
(111, 'Itsbat', '2022-05-08T14_52_49.224Z.wav'),
(112, 'Itsbat', '2022-05-08T14_52_53.034Z.wav'),
(113, 'Itsbat', '2022-05-08T14_52_56.562Z.wav'),
(114, 'Itsbat', '2022-05-08T14_53_00.858Z.wav'),
(115, 'Itsbat', '2022-05-08T14_53_04.201Z.wav'),
(116, 'Itsbat', '2022-05-08T14_53_07.759Z.wav'),
(117, 'Itsbat', '2022-05-08T14_53_18.925Z.wav'),
(118, 'Itsbat', '2022-05-08T14_53_22.868Z.wav'),
(119, 'Itsbat', '2022-05-08T14_53_26.678Z.wav'),
(120, 'Itsbat', '2022-05-08T14_53_29.954Z.wav'),
(121, 'Itsbat', '2022-05-08T14_53_33.460Z.wav'),
(122, 'Itsbat', '2022-05-08T14_53_37.059Z.wav'),
(123, 'Itsbat', '2022-05-08T14_53_44.036Z.wav'),
(124, 'Itsbat', '2022-05-08T14_53_51.085Z.wav'),
(125, 'Itsbat', '2022-05-08T14_54_02.811Z.wav'),
(126, 'Itsbat', '2022-05-08T14_54_06.950Z.wav'),
(127, 'Itsbat', '2022-05-08T14_54_10.552Z.wav'),
(128, 'Itsbat', '2022-05-08T14_54_14.762Z.wav'),
(129, 'Itsbat', '2022-05-08T14_54_19.141Z.wav'),
(130, 'Itsbat', '2022-05-08T14_54_23.622Z.wav'),
(131, 'Itsbat', '2022-05-08T14_54_27.236Z.wav'),
(132, 'Itsbat', '2022-05-08T14_54_40.936Z.wav'),
(133, 'Itsbat', '2022-05-08T14_54_45.152Z.wav'),
(134, 'Itsbat', '2022-05-08T14_54_49.421Z.wav'),
(135, 'Itsbat', '2022-05-08T14_54_53.453Z.wav'),
(136, 'Itsbat', '2022-05-08T14_55_18.610Z.wav'),
(137, 'Itsbat', '2022-05-08T14_55_21.788Z.wav'),
(138, 'Itsbat', '2022-05-08T14_55_25.788Z.wav'),
(139, 'Itsbat', '2022-05-08T14_55_40.307Z.wav'),
(140, 'Itsbat', '2022-05-08T15_01_55.386Z.wav'),
(141, 'Itsbat', '2022-05-08T15_01_59.782Z.wav'),
(142, 'Itsbat', '2022-05-08T15_02_03.951Z.wav'),
(143, 'Itsbat', '2022-05-08T15_02_07.604Z.wav'),
(144, 'Itsbat', '2022-05-08T15_02_11.837Z.wav'),
(145, 'Itsbat', '2022-05-08T15_02_15.676Z.wav'),
(146, 'Itsbat', '2022-05-08T15_02_23.163Z.wav'),
(147, 'Itsbat', '2022-05-08T15_02_27.180Z.wav'),
(148, 'Itsbat', '2022-05-08T15_02_31.167Z.wav'),
(149, 'Itsbat', '2022-05-08T15_02_39.463Z.wav'),
(150, 'Itsbat', '2022-05-08T15_02_47.652Z.wav'),
(151, 'Lana', '2022-05-08T15_45_29.417Z.wav'),
(152, 'Lana', '2022-05-08T15_45_35.387Z.wav'),
(153, 'Lana', '2022-05-08T15_45_41.454Z.wav'),
(154, 'Lana', '2022-05-08T15_45_48.452Z.wav'),
(155, 'Lana', '2022-05-08T15_45_58.203Z.wav'),
(156, 'Lana', '2022-05-08T15_46_02.602Z.wav'),
(157, 'Lana', '2022-05-08T15_46_08.544Z.wav'),
(158, 'Lana', '2022-05-08T15_46_13.018Z.wav'),
(159, 'Lana', '2022-05-08T15_46_18.497Z.wav'),
(160, 'Lana', '2022-05-08T15_46_22.673Z.wav'),
(161, 'Lana', '2022-05-08T15_46_27.020Z.wav'),
(162, 'Lana', '2022-05-08T15_46_31.363Z.wav'),
(163, 'Lana', '2022-05-08T15_46_35.715Z.wav'),
(164, 'Lana', '2022-05-08T15_46_40.671Z.wav'),
(165, 'Lana', '2022-05-08T15_46_45.548Z.wav'),
(166, 'Lana', '2022-05-08T15_46_50.082Z.wav'),
(167, 'Lana', '2022-05-08T15_46_54.082Z.wav'),
(168, 'Lana', '2022-05-08T15_47_07.965Z.wav'),
(169, 'Lana', '2022-05-08T15_47_12.023Z.wav'),
(170, 'Lana', '2022-05-08T15_47_15.468Z.wav'),
(171, 'Lana', '2022-05-08T15_47_18.943Z.wav'),
(172, 'Lana', '2022-05-08T15_47_23.021Z.wav'),
(173, 'Lana', '2022-05-08T15_47_35.199Z.wav'),
(174, 'Lana', '2022-05-08T15_47_39.150Z.wav'),
(175, 'Lana', '2022-05-08T15_47_43.585Z.wav'),
(176, 'Lana', '2022-05-08T15_47_48.036Z.wav'),
(177, 'Lana', '2022-05-08T15_47_52.560Z.wav'),
(178, 'Lana', '2022-05-08T15_48_00.614Z.wav'),
(179, 'Lana', '2022-05-08T15_48_09.715Z.wav'),
(180, 'Lana', '2022-05-08T15_48_23.299Z.wav'),
(181, 'Lana', '2022-05-08T15_48_37.496Z.wav'),
(182, 'Lana', '2022-05-08T15_48_42.393Z.wav'),
(183, 'Lana', '2022-05-08T15_48_47.610Z.wav'),
(184, 'Lana', '2022-05-08T15_48_56.526Z.wav'),
(185, 'Lana', '2022-05-08T15_49_00.813Z.wav'),
(186, 'Lana', '2022-05-08T15_49_14.475Z.wav'),
(187, 'Lana', '2022-05-08T15_49_28.169Z.wav'),
(188, 'Lana', '2022-05-08T15_49_44.925Z.wav'),
(189, 'Lana', '2022-05-08T15_55_15.284Z.wav'),
(190, 'Lana', '2022-05-08T15_55_18.604Z.wav'),
(191, 'Lana', '2022-05-08T15_55_22.243Z.wav'),
(192, 'Lana', '2022-05-08T15_55_25.351Z.wav'),
(193, 'Lana', '2022-05-08T15_55_28.707Z.wav'),
(194, 'Lana', '2022-05-08T15_55_32.215Z.wav'),
(195, 'Lana', '2022-05-08T15_55_35.609Z.wav'),
(196, 'Lana', '2022-05-08T15_55_39.084Z.wav'),
(197, 'Lana', '2022-05-08T15_55_42.343Z.wav'),
(198, 'Lana', '2022-05-08T15_55_45.617Z.wav'),
(199, 'Lana', '2022-05-08T15_55_51.686Z.wav'),
(200, 'Lana', '2022-05-08T15_55_55.080Z.wav'),
(201, 'Ulya', '2022-05-08T15_29_19.962Z.wav'),
(202, 'Ulya', '2022-05-08T15_29_25.629Z.wav'),
(203, 'Ulya', '2022-05-08T15_29_32.403Z.wav'),
(204, 'Ulya', '2022-05-08T15_29_39.128Z.wav'),
(205, 'Ulya', '2022-05-08T15_29_43.872Z.wav'),
(206, 'Ulya', '2022-05-08T15_29_49.361Z.wav'),
(207, 'Ulya', '2022-05-08T15_29_54.354Z.wav'),
(208, 'Ulya', '2022-05-08T15_29_58.436Z.wav'),
(209, 'Ulya', '2022-05-08T15_30_03.233Z.wav'),
(210, 'Ulya', '2022-05-08T15_30_07.790Z.wav'),
(211, 'Ulya', '2022-05-08T15_30_13.010Z.wav'),
(212, 'Ulya', '2022-05-08T15_30_17.809Z.wav'),
(213, 'Ulya', '2022-05-08T15_30_22.464Z.wav'),
(214, 'Ulya', '2022-05-08T15_30_27.507Z.wav'),
(215, 'Ulya', '2022-05-08T15_30_32.364Z.wav'),
(216, 'Ulya', '2022-05-08T15_30_36.951Z.wav'),
(217, 'Ulya', '2022-05-08T15_30_41.738Z.wav'),
(218, 'Ulya', '2022-05-08T15_31_01.123Z.wav'),
(219, 'Ulya', '2022-05-08T15_31_07.572Z.wav'),
(220, 'Ulya', '2022-05-08T15_31_13.539Z.wav'),
(221, 'Ulya', '2022-05-08T15_31_17.695Z.wav'),
(222, 'Ulya', '2022-05-08T15_31_27.716Z.wav'),
(223, 'Ulya', '2022-05-08T15_31_32.643Z.wav'),
(224, 'Ulya', '2022-05-08T15_31_37.706Z.wav'),
(225, 'Ulya', '2022-05-08T15_31_47.069Z.wav'),
(226, 'Ulya', '2022-05-08T15_31_52.432Z.wav'),
(227, 'Ulya', '2022-05-08T15_31_57.392Z.wav'),
(228, 'Ulya', '2022-05-08T15_32_01.889Z.wav'),
(229, 'Ulya', '2022-05-08T15_32_11.819Z.wav'),
(230, 'Ulya', '2022-05-08T15_32_21.404Z.wav'),
(231, 'Ulya', '2022-05-08T15_32_26.204Z.wav'),
(232, 'Ulya', '2022-05-08T15_32_37.585Z.wav'),
(233, 'Ulya', '2022-05-08T15_32_49.468Z.wav'),
(234, 'Ulya', '2022-05-08T15_33_03.742Z.wav'),
(235, 'Ulya', '2022-05-08T15_33_08.633Z.wav'),
(236, 'Ulya', '2022-05-08T15_33_14.066Z.wav'),
(237, 'Ulya', '2022-05-08T15_33_23.811Z.wav'),
(238, 'Ulya', '2022-05-08T15_33_46.203Z.wav'),
(239, 'Ulya', '2022-05-08T15_33_50.380Z.wav'),
(240, 'Ulya', '2022-05-08T15_33_59.135Z.wav'),
(241, 'Ulya', '2022-05-08T15_40_46.715Z.wav'),
(242, 'Ulya', '2022-05-08T15_40_50.746Z.wav'),
(243, 'Ulya', '2022-05-08T15_40_54.605Z.wav'),
(244, 'Ulya', '2022-05-08T15_40_58.439Z.wav'),
(245, 'Ulya', '2022-05-08T15_41_02.273Z.wav'),
(246, 'Ulya', '2022-05-08T15_41_05.816Z.wav'),
(247, 'Ulya', '2022-05-08T15_41_09.421Z.wav'),
(248, 'Ulya', '2022-05-08T15_41_13.003Z.wav'),
(249, 'Ulya', '2022-05-08T15_41_19.461Z.wav'),
(250, 'Ulya', '2022-05-08T15_41_23.139Z.wav');

-- --------------------------------------------------------

--
-- Table structure for table `hyperparam`
--

CREATE TABLE `hyperparam` (
  `id` int(11) NOT NULL,
  `epoch` int(11) NOT NULL,
  `bs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hyperparam`
--

INSERT INTO `hyperparam` (`id`, `epoch`, `bs`) VALUES
(1, 4, 32);

-- --------------------------------------------------------

--
-- Table structure for table `log_identifikasi`
--

CREATE TABLE `log_identifikasi` (
  `id` int(11) NOT NULL,
  `voice_name` varchar(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `tgl` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log_identifikasi`
--

INSERT INTO `log_identifikasi` (`id`, `voice_name`, `result`, `tgl`) VALUES
(1, '2022-05-22T155406.676Z.wav', 'Lana', '2022-05-22 22:54:11'),
(2, '2022-05-22T155710.713Z.wav', 'Ulya', '2022-05-22 22:57:16'),
(3, '2022-05-23T005240.129Z.wav', 'Ulya', '2022-05-23 07:52:43'),
(4, '2022-05-23T031955.028Z.wav', 'Ulya', '2022-05-23 10:20:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `nama`, `username`, `password`) VALUES
(1, 'Admin', 'admin', 'admin'),
(2, 'Faisol Gans', 'faisol', 'faisol');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dataset`
--
ALTER TABLE `dataset`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hyperparam`
--
ALTER TABLE `hyperparam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log_identifikasi`
--
ALTER TABLE `log_identifikasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dataset`
--
ALTER TABLE `dataset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=252;

--
-- AUTO_INCREMENT for table `hyperparam`
--
ALTER TABLE `hyperparam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `log_identifikasi`
--
ALTER TABLE `log_identifikasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
