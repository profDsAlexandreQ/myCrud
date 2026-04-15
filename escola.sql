Create database escola;
use escola;
create table aluno (
    id int primary key auto_increment,
    nome varchar(255) not null,
    idade int not null,
    email varchar(255) not null
);
create table curso (
    id int primary key auto_increment,
    nome varchar(255) not null,
    descricao text
);
create table matricula (
    id int primary key auto_increment,
    aluno_id int,
    curso_id int,
    data_matricula date,
    foreign key (aluno_id) references aluno(id),
    foreign key (curso_id) references curso(id)
);