import { defineStore } from 'pinia'

export const studentsStore = defineStore('students', {
  state: () => ({
    students: [],
  }),
  actions:{
    initFromApi(){
      this.students = ["Test123", "Test456"]

    }
  }
})