/** @odoo-module */

import { loadCSS, loadJS } from "@web/core/assets";
const { Component, onMounted, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks"

export class Equipes extends Component {
    setup() {
        this.rpc = useService("rpc");

        onMounted(async () => {
            this.mountInputs()
        })
    }

    async mountInputs() {
        const props = this.props

        this.allEquipes = await this.rpc(`/hr_management/pointage/get_all_Equipes`);

        $('#select-equipe').selectize({
            maxItems: 1,
            minItems: 1,
            valueField: 'id',
            labelField: 'name',
            searchField: 'name',
            options: this.allEquipes,
            create: false,
            onChange: function (value) {
                props.onChangeEquipe(value);
            }
        });
    }
}

Equipes.template = "owl.equipes"