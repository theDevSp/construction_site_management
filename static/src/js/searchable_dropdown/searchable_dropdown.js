/** @odoo-module **/

const { loadJS, loadCSS } = require('@web/core/assets');
import { Component, onWillStart ,onMounted} from "@odoo/owl"
import { useService } from "@web/core/utils/hooks"


export class ChantierDrop extends Component {
    setup() {

        this.rpc = useService("rpc");

        onWillStart(async () => {
            await loadJS("/reports_templates/static/src/lib/selectize/selectize.min.js")
            await loadCSS("/reports_templates/static/src/lib/selectize/selectize.default.min.css")
            
        })

        onMounted(async() =>{
            this.chantierList()
        })


    }

    async chantierList() {
        this.allChantiers = await this.rpc("/construction_site_management/get_all_chantiers")
        $('.select-chantier-component').selectize({
            maxItems: 1,
            minItems: 1,
            valueField: 'id',
            labelField: 'name',
            searchField: 'name',
            options: this.allChantiers,
            create: false
        });
    }

}

ChantierDrop.template = "construction_site_management.dropdown"
