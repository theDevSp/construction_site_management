/** @odoo-module **/

import { Dropdown } from "@web/core/dropdown/dropdown"
import { DropdownItem } from "@web/core/dropdown/dropdown_item"
import { useService } from "@web/core/utils/hooks"
import { Component, useSubEnv, onWillStart, useEffect, useState, useRef } from "@odoo/owl"


export class ChantierDrop extends Component {
    setup() {

        this.state = useState({
            display_name: 'Choisir un Chantier',
            chantierList: [],
            tempchantierList: []
        })

        this.searchInput = useRef("searchInput")
        this.toggler = useRef("toggler-div")
        this.chantier_service = useService("chantierListService")
        onWillStart(() => this.chantierList())
        useEffect(() => {
            this.styling_component()
        })
    }


    styling_component() {
        this.toggler.el.querySelector('.dropdown-toggle').classList.add("form-select");
    }

    selected(chantier) {
        this.state.display_name = chantier.code + ' - ' + chantier.name
    }
    chantierList() {
        const chantier_service = this.env.services.chantierListService
        chantier_service.chantierlist.then((result) => {
            result.result.forEach(element => {
                this.state.chantierList.push(element)
                this.state.tempchantierList.push(element)
            });

        })
        
    }


    async searchTasks() {
        const text = this.searchInput.el.value

        if (text.length === 0) {
            this.state.chantierList = this.state.tempchantierList
        } else {
            this.state.chantierList = this.state.chantierList.filter(chantier => String(chantier.name).toLowerCase().includes(text) || String(chantier.code).toLowerCase().includes(text))
        }
    }
}

ChantierDrop.template = "construction_site_management.dropdown"
ChantierDrop.components = { Dropdown, DropdownItem }