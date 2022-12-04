/// <reference types="cypress" />

describe("title", () => {
    it("opens web app", () => {
        cy.visit('http://localhost:5000')
    })

    it("inputs text", () => {
        const newEntityText = "Nikola Tesla was a Serbian-American inventor from Smiljan. He was able to speak English among other languages."
        cy.get('[id=input-text]').type(`${newEntityText}`)
    })

    it("clicks find button", () => {
        cy.get("[id=find-button]").click()
    })

    it("lists entities correctly", () => {
        cy.get(".ner-row").eq(0).should('have.text', 'Nikola TeslaPerson')
        cy.get(".ner-row").eq(1).should('have.text', 'SerbianGroup')
        cy.get(".ner-row").eq(2).should('have.text', 'SmiljanLocation')
        cy.get(".ner-row").eq(3).should('have.text', 'EnglishLanguage')
    })
})