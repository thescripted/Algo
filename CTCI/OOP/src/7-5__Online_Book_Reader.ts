class OnlineReaderSystem {
  library: Library;
  userManager: UserManager;
  display: Display;

  activeUser: User;
  activeBook: Book;

  constructor() {
    this.userManager = new UserManager();
    this.library = new Library();
    this.display = new Display();
  }

  getLibrary(): Library {
    return this.library;
  }

  getUserManager(): UserManager {
    return this.userManager;
  }

  getDisplay(): Display {
    return this.display;
  }

  getActiveBook(): Book {
    return this.activeBook;
  }

  getActiveUser(): User {
    return this.activeUser;
  }

  setActiveBook(book: Book) {
    this.activeBook = book;
    this.display.displayBook(book);
  }

  setActiveUser(user: User) {
    this.activeUser = user;
    this.display.displayUser(user);
  }
}

class Library {}

class Book {}

class UserManager {}

class Display {}

class User {}
