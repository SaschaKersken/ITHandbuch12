SET NAMES utf8;
CREATE TABLE languages (
    language_id int auto_increment,
    language_name varchar(30),
    language_architecture enum('imperative', 'oop', 'other'),
    language_implementation enum('compiler', 'interpreter', 'VM', 'other'),
    language_system set('Unix', 'Windows', 'sonstige'),
    language_description varchar(255),
    language_year year,
    primary key(language_id),
    index(language_name)
);
INSERT INTO languages (
    language_name,
    language_architecture,
    language_implementation,
    language_system,
    language_description,
    language_year
)
VALUES
('C', 'imperative', 'compiler', 'Unix,Windows,other', 'Klassische Programmiersprache, die zur Neuimplementierung von UNIX entwickelt wurde. Ihre Syntax inspirierte viele andere Sprachen.', 1970),
('C++', 'oop', 'compiler', 'Unix,Windows,other', 'Weiterentwicklung von C mit OOP-Fähigkeiten', 1983),
('Python', 'oop', 'interpreter', 'Unix,Windows,other', 'Moderne Multiparadigmen-Skriptsprache mit objektorientierten und funktionalen Aspekten', 1990),
('Ruby', 'oop', 'interpreter', 'Unix,Windows,other', 'Skriptsprache mit fast allen Perl-Features sowie sauberer, moderner OOP-Implementierung', 1993),
('Java', 'oop', 'VM', 'Unix,Windows,other', 'OOP-Sprache mit Multi-Plattform-VM', 1995),
('Perl', 'imperative', 'interpreter', 'Unix,Windows,other', 'Skriptsprache für Admin- und Textbearbeitungsaufgaben; neuere Versionen bieten (umständliche) OOP.', 1987),
('JavaScript', 'other', 'interpreter', 'Unix,Windows,other', 'Skriptsprache, die vor allem in Browsern verwendet wird', 1995),
('Scala', 'other', 'VM', 'Unix,Windows,other', 'Funktionale Sprache für die Java-VM', 2003);
