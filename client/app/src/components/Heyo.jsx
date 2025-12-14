import { useEffect, useState } from 'react'

import '../App.css'

function Oncekiler() {
  const [books, setBooks] = useState([])
  const [book, setBook] = useState({
    title: "",
    releaseYear: 0
  })
  const [newTitle, setNewTitle] = useState("");

  useEffect(() =>{
    fetchBooks();

  }, [])

  const fetchBooks = async () =>{
    try{
      const response = await fetch("http://127.0.0.1:8000/api/books/")
      const data = await response.json()
      console.log(data)
      setBooks(data)
    }catch(err){
      console.log(err)
    }
  }
  
function handleNewTitle(event){
  const {name, value} = event.target;

  setNewTitle(value)
}

  function handleChange(event){
    const {name, value} = event.target; 

    setBook(prevData =>{
      return {
        ...prevData,
        [name]: value
      }
    })

  }
  
  const updateTitle = async (pk, releaseYear) =>{
    const bookData = {
      book_name: newTitle,
      release_date: releaseYear,
    };
    try{
    const response = await fetch(`http://127.0.0.1:8000/api/books/${pk}`, {
      method: "PUT",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookData),
    });
    const data = await response.json()
    console.log(data)
    setBooks(prevBooks =>{
      return prevBooks.map(book =>{
        if (book.id === pk){
          return data;
        }
        return book
      })
    })
    }catch(err){
      console.log(err)
    }

  }

  const addBook = async () =>{
    const bookData = {
      bookTitle: book.title,
      releaseYear: book.releaseYear,
    }
    try{
    const response = await fetch("http://127.0.0.1:8000/api/books", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookData),
    });
    const data = await response.json()
    console.log(data)
    
    }catch(err){
      console.log(err)
    }

  }

  const deleteBook = async (pk) => {
    try{
      const response = await fetch(`http://127.0.0.1:8000/api/books/${pk}`, {
      method: "DELETE",
    });
    setBooks(prev => prev.filter(book => book.id !== pk))

    } catch(err){
      console.log(err)

    }
  }

  return (
    <>
      <h1>Book Website</h1>
      <p>
        Input-Name : {book.title} 
      </p>
      <p>
        Input-Year : {book.releaseYear}
      </p>

      <div>
        <input type="text" onChange={handleChange} name='title' placeholder='Book Title...' />
        <input type="number" onChange={handleChange} name='releaseYear' placeholder='Release Year...' />
        <button onClick={addBook}>Add Book</button>
      </div>
      {books.map((book, index) =>
      <div key={index}>
        <p key={book.id}>Title: {book.book_name}
          <br/>
          Release Year: {book.release_date}
        </p>
        <input type="text" onChange={handleNewTitle} placeholder='New Title...'/>
        <button onClick={() => updateTitle(book.id, book.releaseYear)}>Change Title</button>
        <button onClick={() => deleteBook(book.id)}>Delete Book</button>

      </div>)}
    </>
  )
}

export default Oncekiler;
