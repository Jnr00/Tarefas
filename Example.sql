CREATE TABLE Biblioteca (
  id integer PRIMARY KEY,
  nome TEXT not null,
  autor TEXT not null,
  genero TEXT not null
);

INSERT INTO BIBLIOTECA values(1,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(2,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(3,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(4,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(5,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(6,pequeno principe,saint-exupery,fantasia)
INSERT INTO BIBLIOTECA values(7,pequeno principe,saint-exupery,fantasia)

SELECT id,nome from Biblioteca 
