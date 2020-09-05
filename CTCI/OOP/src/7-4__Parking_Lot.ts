// 7.4 Parking Lot: Design a Parking Lot using Object-Oriented Principles

enum VehicleSize {
  MOTORCYCLE,
  COMPACT,
  LARGE
}

abstract class Vehicle {
  licensePlate: string;
  spotsNeeded: number;
  size: VehicleSize;

  getSpotsNeeded(): number {
    return this.spotsNeeded;
  }

  getSize(): VehicleSize {
    return this.size;
  }
}
