/** @odoo-module */

import { registry } from "@web/core/registry"

export const chantierListService = {
    dependencies:["orm", "user", "rpc","notification"],
    async start(env, { orm, user, rpc, notification }){

        async function fetchChantierList(){
            
            
            return await rpc("/construction_site_management/get_all_chantiers")
        }
    
        return {
            chantierlist:fetchChantierList()
        }
    }
}

registry.category('services').add("chantierListService", chantierListService)