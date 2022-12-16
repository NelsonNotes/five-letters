import { createAsyncThunk } from '@reduxjs/toolkit'
import { sessionAPI } from '../../api/session'

export const fetchSession = createAsyncThunk(
	'session/fetchSession',
	async () => {
		return await sessionAPI.getSession({
			username: 'nikitazharov2',
			password: 'super-secret-password',
		})
	}
)
