create table guest (
    guestid int primary key identity(1,1), 
    name nvarchar(100) not null, 
    phone nvarchar(15) not null,
    email nvarchar(100) unique, 
    address nvarchar(255)
);

create table room (
    roomid int primary key identity(1,1),
    roomtype nvarchar(50) not null, 
    pricepernight decimal(10, 2) not null check (pricepernight > 0),
    status nvarchar(20) not null
);

create table reservation (
    reservationid int primary key identity,
    guestid int not null,
    roomid int not null,
    checkindate date not null,
    checkoutdate date not null,
    totalamount int not null,
    foreign key (guestid) references guest(guestid),
    foreign key (roomid) references room(roomid)
);

create table service (
    serviceid int primary key identity (1,1),
    servicename nvarchar(100) not null,
    description nvarchar(255),
    price decimal(10, 2) not null check (price >= 0)
);

create table reservationservice (
    reservationserviceid int primary key identity (1,1),
    reservationid int not null,
    serviceid int not null,
    quantity int not null check (quantity > 0),
    foreign key (reservationid) references reservation(reservationid),
    foreign key (serviceid) references service(serviceid)
);
