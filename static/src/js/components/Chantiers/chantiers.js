/** @odoo-module */

import { loadCSS, loadJS } from "@web/core/assets";
const { Component, onMounted, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks"

export class Chantiers extends Component {
    setup() {
        this.rpc = useService("rpc");

        onMounted(async () => {
            this.mountInputs()
        })
    }

    async mountInputs() {

        const props = this.props
        this.allChantiers = await this.rpc(`/hr_management/pointage/get_all_chantiers`);

        $('#select-chantier').selectize({
            maxItems: 1,
            minItems: 1,
            valueField: 'id',
            labelField: 'name',
            searchField: 'name',
            options: this.allChantiers,
            create: false,
            onChange: function (value) {
                props.onChangeChantier(value);
            }
        });

    }


}

Chantiers.template = "owl.chantiers"