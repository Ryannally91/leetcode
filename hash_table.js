class HashTable {
    constructor() {
        this.table = new Array(127); // how do I know what set array size to? 127 main AScii chars?
        this.size = 0;
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash += key.charCodeAt(i);
        }
        return hash % this.table.length;
    }

    //Is set both updating index and adding to it?

    set(key, value) {
        const index = this._hash(key);
        if (this.table[index]) {
            for (let i = 0; i < this.table[index].length; i++) {
                //is this.table[index].length accounting for chaining
                if (this.table[index][i][0] === key) {
                    this.table[index][i][1] = value;
                    return;
                }
            }
            this.table[index].push([key, value]);
        } else {
            this.table[index] = [];
            this.table[index].push([key, value]);
        }
        this.size++;
    }

    get(key) {
        const index = this._hash(key);
        if (this.table[index]) {
            for (let i = 0; i < this.table.length; i++) {
                if (this.table[index][i][0] === key) {
                    return this.table[index][i][1];
                }
            }
        }
        return undefined;
    }

    remove(key) {
        const index = this._hash(key);

        if (this.table[index] && this.table[index].length) {
            for (let i = 0; i < this.table.length; i++) {
                if (this.table[index][i][0] === key) {
                    this.table[index].splice(i, 1);
                    this.size--;
                    return true;
                }
            }
        } else {
            return false;
        }
    }

    display() {
        this.table.forEach((values, index) => {
            const chainedValues = values.map(
                ([key, value]) => `[ ${key}: ${value} ]`
            );
            console.log(`${index}: ${chainedValues}`);
        });
    }
}

const newTable = new HashTable();
newTable.set("mark", 17);
newTable.set("mike", 17);
newTable.set("mrak", 7);
newTable.display();
newTable.set("mark", 20);
newTable.display();

////////////
function HashMap(capacity) {
    this.capacity = capacity; //limit
    this.table = [];
}
// -usamos esta línea para codificar una cadena ...
var myHashCode = myString.hashCode();
// ...basada en esta implementación:
String.prototype.hashCode = function () {
    var hash = 0;
    if (this.length == 0) return hash;
    for (i = 0; i < this.length; i++) {
        char = this.charCodeAt(i);
        hash = (hash << 5) - hash + char;
        hash &= hash; //Convert-->32b int
    }
    return hash;
};
// JS % actúa de forma extraña con los negativos,
// ...y lo usamos de esta manera:
function mod(input, div) {
    return ((input % div) + div) % div;
}
// ... and we use it this way:
var myIdx = mod(myHashCode, arrSize);
