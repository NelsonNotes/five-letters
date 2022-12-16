import { TUserResponse } from '../types/user'
import { customFetch } from './utils'

export const userAPI = {
	getUser: (): Promise<TUserResponse> => customFetch('/user/', 'GET'),
}
