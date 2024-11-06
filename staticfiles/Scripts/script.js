class Transport {
    constructor(fuel, title) {
        this.fuel = fuel
        this.title = title
    }
    toString(){
        return `${this.fuel}litres ${this.title}`
    }
}

class Car extends Transport {
    constructor(fuel, title, sScolor, typeWheels) {
        super(fuel, title);
        this.SScolor = sScolor;
        this.HappyWheels = typeWheels;
    }

    Bibika() {
        return "woaw"
    }
}

class Boat extends Transport {
    constructor(fuel, title, bColor, seatMaterial) {
        super(fuel, title);
        this.bColor = bColor;
        this.seatMaterial = seatMaterial;
    }
}
const a = new Car(1, 'a', 'b', 'c')
const b = new Boat(120, 'b','c','d')
const t = new Transport(2,'wertolet')
const v = [a,b,t]